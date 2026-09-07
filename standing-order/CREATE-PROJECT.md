# Standing Order — Project Creation

*From the zip to a working repo with the Unity project inside it. Numbered, in order.*

You have `standing-order.zip`. Everything below is copy-paste.

---

## 1 — Unpack it

Unzip into your `Fun Game Stuff` folder. You should end up with:

```
Fun Game Stuff/
  standing-order/
    CLAUDE.md  README.md  SETUP.md  WALKTHROUGH.md
    .gitignore  .gitattributes  .editorconfig
    .github/workflows/core-tests.yml
    docs/        23 specification documents
    prototype/   the working simulation
    core/  adapter/  unity/  tools/    (empty, with .gitkeep)
```

**macOS:** press **Cmd+Shift+.** in Finder to see the dotfiles. They're there either way.

---

## 2 — Make it a repository

```
cd "Fun Game Stuff/standing-order"
git init
git lfs install
git add .
git commit -m "Project setup: specification set, agent instructions, repo config"
```

**Check:** `git status` says clean, and `git log` shows one commit.

**Why now:** `.gitattributes` is committed before any binary file exists. Retrofitting LFS onto a repo that already has assets is genuinely miserable.

---

## 3 — Core and its tests

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

**Check:** `dotnet test` passes with zero tests.

```
git add .
git commit -m "Core project skeleton and test harness"
```

---

## 4 — Push, and watch CI fail

Create an empty repo on GitHub, then:

```
git remote add origin <your-repo-url>
git branch -M main
git push -u origin main
```

Now add a deliberately broken test in `core/StandingOrder.Core.Tests/UnitTest1.cs`:

```csharp
[Fact] public void Deliberately_Broken() => Assert.True(false);
```

Push it. Watch the **Actions** tab go red. Delete it. Push. Watch it go green.

**Check:** you have personally seen CI fail. Don't skip — an unverified pipeline is worse than none, because you'll trust it.

---

## 5 — Point Claude Code at it

Open the Code tab (or `claude` in a terminal) at `Fun Game Stuff/standing-order`.

Ask it, before any work:

> What is this project's one architectural rule?

It should say Core has no Unity references, unprompted. If it doesn't, you've opened the wrong folder — it needs `CLAUDE.md` at the root of what it opens.

---

## 6 — First real task

> Read CLAUDE.md and docs/standing-order-project-setup.md. Implement task A2: the static data tables for 16 chambers, 25 tunnels, 6 latent connections and 4 camps, exactly as specified in docs/00-MASTER-standing-order.md Part 2. Plain C# in core/StandingOrder.Core, loaded from a data file rather than hard-coded. Add validation tests asserting no chamber is held by two camps, every tunnel references a real chamber, and every camp's seat is among its holdings. Do not touch the unity/ folder.

**Check:** `dotnet test` passes with the new tests, CI green.

Then A3 through A9 in order, from the task table in the setup document.

---

## 7 — The Unity project, when you want it

It goes **inside** the repo, at `standing-order/unity/`.

1. Unity Hub → **Installs** → install the newest **6000.3.x** (Unity 6.3 LTS — supported to December 2027; 6.0 LTS expires October 2026, and 6.6 is an update release, not LTS)
2. Hub → **Projects** → **New project**
3. Template: **Universal 3D** (URP)
4. Name: `unity`
5. Location: `Fun Game Stuff/standing-order` — so it lands at `standing-order/unity/`
6. Create

The `unity/` folder already exists with a `.gitkeep`; delete that once Unity has populated it.

Then immediately, **Edit → Project Settings**:

| Section | Setting | Value |
|---|---|---|
| Editor | Asset Serialization → Mode | **Force Text** |
| Editor | Version Control → Mode | **Visible Meta Files** |
| Player | Other Settings → Colour Space | **Linear** |

**Check:** `git status` shows `.asset` and `.meta` files as readable text, not binary.

```
git add .
git commit -m "Unity project, URP, text serialisation"
```

---

## 8 — Unity MCP, when you reach Phase D

1. **Window → Package Manager → Unity Registry** → install **AI Assistant**
2. **Edit → Project Settings → AI → Unity MCP** → confirm **Unity Bridge: Running** (green)
3. Same page → expand **Integrations** → **Claude Code** → **Configure**

**Check:** with Unity open, ask Claude Code *"what objects are in the current scene?"*

---

## 9 — Blender MCP, when you reach whiteboxing

```
claude mcp add --scope user blender -- uvx blendmcp
```

Then install the Blender add-on and start its server from the sidebar panel.

**Check:** with Blender open, ask *"what objects are in the current Blender scene?"*

Run only one instance of the Blender MCP server — don't have Claude Desktop and Claude Code both live on it at once.

---

## The whole thing

Unzip → `git init` and commit → Core and tests → push and watch CI fail → Claude Code on the repo → task A2 → work through A3–A9 → **then** Unity inside `unity/` → MCP at Phase D → Blender at whiteboxing.

Steps 1 to 4 are about an hour. Everything after that is building.
