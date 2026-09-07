# Standing Order — Literal Setup Walkthrough

*Click by click, from an empty machine. v0.1, September 2026.*

Where a step differs on macOS and Windows it is marked. Verify each **Check** before moving on.

---

# STEP 1 — Install Unity Hub

1. Go to **unity.com/download**
2. Download **Unity Hub** for your OS
3. Install it and sign in (create a free Unity account if you don't have one)
4. In Hub → **Preferences → Licenses → Add** → **Get a free personal licence**

**Check:** Unity Hub opens and shows a valid licence.

---

# STEP 2 — Install the right Unity version

**Use Unity 6.3 LTS (version string `6000.3.x`).**

Why this one: <cite index="25-1">Unity 6.3 LTS is supported until December 2027, while Unity 6.0 LTS is supported through October 2026</cite> — 6.0 runs out next month. And <cite index="24-1">Unity AI is available in Beta in Unity 6.3 LTS</cite>, which is what carries the official MCP server.

Do **not** take Unity 6.6 even though it is newer. It is an update release, not LTS.

1. Hub → **Installs** → **Install Editor**
2. Pick the newest **6000.3.x** entry marked LTS. If it isn't listed, use the **Archive** / version-search box
3. In the modules list tick:
   - **Universal Render Pipeline** (if offered as a template module)
   - **Windows Build Support (IL2CPP)** *or* **Mac Build Support (IL2CPP)** — whichever you are *not* on, plus your own platform
   - **Documentation**
4. Install. This takes a while

**Check:** Hub → Installs shows `6000.3.x` with a green tick.

---

# STEP 3 — Install the supporting tools

**macOS** (with Homebrew):
```
brew install git git-lfs dotnet-sdk node
git lfs install
```

**Windows** (with winget):
```
winget install Git.Git
winget install GitHub.GitLFS
winget install Microsoft.DotNet.SDK.8
winget install OpenJS.NodeJS.LTS
git lfs install
```

Then install the Claude Code CLI:
```
npm install -g @anthropic-ai/claude-code
```

**Check:** each of these prints a version — `git --version`, `git lfs version`, `dotnet --version`, `node --version`, `claude --version`.

---

# STEP 4 — Authenticate Claude Code

```
claude auth login
```

<cite index="34-1">This opens a browser window for OAuth login. Sign in with your Anthropic account. After login, verify your subscription is active by running claude interactively and checking the status line shows your plan rather than Claude API.</cite>

**Check:** `claude` opens, and the status line names your plan.

---

# STEP 5 — Create the repository

```
mkdir standing-order && cd standing-order
git init
mkdir -p docs prototype core adapter unity tools .github/workflows
```

Copy in the files I've given you:

| File | Goes to |
|---|---|
| `CLAUDE.md` | repo root |
| `README.md` | repo root |
| `SETUP.md` | repo root |
| `gitignore.txt` | repo root, **renamed `.gitignore`** |
| `gitattributes.txt` | repo root, **renamed `.gitattributes`** |
| `editorconfig.txt` | repo root, **renamed `.editorconfig`** |
| `ci-dotnet-tests.yml` | `.github/workflows/` |
| every `standing-order-*.md`, `00-MASTER-*.md`, `00-index.md` | `docs/` |
| `deepholt_simulation.html` | `prototype/` |

```
git add .
git commit -m "Project setup: specification set, agent instructions, repo config"
```

**Check:** `git status` is clean and `.gitattributes` is committed **before** any binary file exists.

---

# STEP 6 — Core and tests, before Unity

```
cd core
dotnet new classlib -o StandingOrder.Core
dotnet new xunit -o StandingOrder.Core.Tests
cd StandingOrder.Core.Tests
dotnet add reference ../StandingOrder.Core/StandingOrder.Core.csproj
cd ..
dotnet new sln -n StandingOrder
dotnet sln add StandingOrder.Core/StandingOrder.Core.csproj
dotnet sln add StandingOrder.Core.Tests/StandingOrder.Core.Tests.csproj
dotnet test
cd ..
```

**Check:** `dotnet test` passes. Commit.

---

# STEP 7 — Prove CI fails

Push to GitHub, then add a deliberately broken test:

```csharp
[Fact] public void Deliberately_Broken() => Assert.True(false);
```

Push. Watch the Actions tab go red. Delete the test, push, watch it go green.

**Check:** you have personally seen CI fail. Skip this and you will trust a pipeline that may not run.

---

# STEP 8 — Create the Unity project

1. Hub → **Projects** → **New project**
2. Editor version: your **6000.3.x**
3. Template: **Universal 3D** (URP)
4. Project name: `unity`
5. Location: the `standing-order/` folder — so it lands at `standing-order/unity/`
6. Create. First open takes several minutes

**Check:** the editor opens on a sample scene.

---

# STEP 9 — Unity settings, immediately

In the editor, **Edit → Project Settings**:

| Section | Setting | Value |
|---|---|---|
| **Editor** | Asset Serialization → Mode | **Force Text** |
| **Editor** | Version Control → Mode | **Visible Meta Files** |
| **Editor** | Enter Play Mode Settings | leave **Reload Domain ON** |
| **Player** | Other Settings → Colour Space | **Linear** |

Then in the Project window: delete the sample scene contents, and create folders `Assets/Scenes`, `Assets/Scripts`, `Assets/Audio`, `Assets/Art`, `Assets/UI`.

**Check:** `git status` shows `.asset` and `.meta` files as readable text, not binary.

---

# STEP 10 — Install the Unity AI package (this carries MCP)

<cite index="39-1">Unity's official MCP Server is included with the in-editor AI assistant package.</cite>

1. **Window → Package Manager**
2. **Unity Registry** tab
3. Search for **AI Assistant**, install it
4. Restart the editor if prompted

**Check:** **Edit → Project Settings** now shows an **AI** section.

---

# STEP 11 — Turn on the MCP bridge

<cite index="42-1">Go to Edit > Project Settings > AI > Unity MCP. Confirm the Unity Bridge status shows Running (green indicator). The bridge starts automatically when the editor loads. If it shows Stopped, select Start.</cite>

<cite index="42-1">The relay binary is automatically installed to ~/.unity/relay/ when the editor starts.</cite>

**Check:** Unity Bridge shows **Running**, green.

---

# STEP 12 — Connect Claude Code to Unity

<cite index="39-1">The Integrations section of the Unity MCP settings page can automatically configure supported clients – expand Integrations, select your client, and select Configure.</cite> <cite index="39-1">Supported clients may include Claude Code, Cursor, Windsurf, and Claude Desktop, depending on your Unity MCP version.</cite>

1. Same settings page → expand **Integrations**
2. Find **Claude Code** → **Configure**

If Claude Code isn't in the auto-configure list: <cite index="39-1">add a server entry pointing to the Unity relay binary, installed to ~/.unity/relay/, passing --mcp as a command-line argument.</cite>

**Check:** with Unity open, run `claude` from `standing-order/` and ask *"what objects are in the current scene?"* It should answer from the live editor.

---

# STEP 13 — First agent session

From `standing-order/`:

```
claude
```

First, confirm it has read the instructions:

> What is this project's one architectural rule?

It should say Core has no Unity references, unprompted. If it doesn't, `CLAUDE.md` isn't at the repo root.

Then:

> Read CLAUDE.md and docs/standing-order-project-setup.md. Implement task A2: the static data tables for 16 chambers, 25 tunnels, 6 latent connections and 4 camps, exactly as specified in docs/00-MASTER-standing-order.md Part 2. Plain C# in core/StandingOrder.Core, loaded from a data file rather than hard-coded. Add validation tests asserting no chamber is held by two camps, every tunnel references a real chamber, and every camp's seat is among its holdings. Do not touch the Unity project.

**Check:** `dotnet test` passes with the new tests, and CI is green.

---

# What you do NOT install yet

**Wwise.** Wait until layer four, then pin the Unity and Wwise versions together and freeze both.

**Unity AI Generators.** The Assistant package is installed for MCP. Leave asset generation off — <cite index="20-1">world generation got stuck twice and it is described as an exciting foundation that is not yet ready for real production work</cite>, and your art direction is silhouette-led, which is where generic generation is weakest.

**The Unity AI Gateway.** It looks like the obvious way to use Claude inside Unity, and it isn't worth it: <cite index="19-1">it requires an active Unity AI subscription on top, and accepts only API keys — not consumer subscriptions like Claude Pro or ChatGPT Plus</cite>. The MCP route above gives you Claude Code with live project awareness at no extra cost.

---

# The whole thing in order

Unity Hub → **6.3 LTS** → git, lfs, dotnet, node, claude → `claude auth login` → repo and files → **Core and tests before Unity** → watch CI fail → Unity project at `unity/` → Force Text and Linear → AI Assistant package → MCP bridge running → Integrations → Configure Claude Code → first task.

Roughly half a day, most of it downloads.
