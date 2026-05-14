# Codex Adapter

This directory contains a local Codex Skill adaptation of the original Claude Code Vibe Noveling workflow.

## Install

Copy the skill folder into your Codex skills directory:

```powershell
Copy-Item -LiteralPath .\codex\skills\vibe-noveling -Destination "$env:USERPROFILE\.codex\skills\vibe-noveling" -Recurse -Force
```

Then start a new Codex session and invoke it with:

```text
Use $vibe-noveling to initialize a local Chinese web novel project.
```

## What It Provides

- local project initialization
- worldbuilding and plot discussion workflow
- full-book, volume, and chapter planning
- chapter drafting and revision workflow
- knowledge graph, name generation, snapshots, progress chart, and word-count helper scripts

The original `/novel-*` slash commands are interpreted as local Codex workflow requests rather than Claude Code commands.
