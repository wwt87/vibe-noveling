# Codex Adapter

This directory contains a local Codex Skill adaptation of the original Claude Code Vibe Noveling workflow.

The original project is organized around Claude Code slash commands and agents. The Codex adapter packages the same workflow as a discoverable Codex Skill, so Codex can operate through local files, references, and helper scripts.

## Install

From the repository root:

```powershell
Copy-Item -LiteralPath .\codex\skills\vibe-noveling -Destination "$env:USERPROFILE\.codex\skills\vibe-noveling" -Recurse -Force
```

Start a new Codex session after installation. Then invoke it naturally:

```text
Use $vibe-noveling to initialize a local Chinese web novel project.
```

Chinese example:

```text
用 $vibe-noveling 初始化一个都市小说项目，书名《一个失业的39岁程序员》
```

## Command Mapping

The original `/novel-*` commands are interpreted as local Codex workflow requests:

| Original command | Codex local behavior |
| --- | --- |
| `/novel-init` | Create project skeleton, `CLAUDE.md`, `memory/`, `chapters/`, templates, snapshots |
| `/novel-discuss` | Discuss worldbuilding, characters, systems, and future plot; write confirmed decisions to `memory/` |
| `/novel-bookplan` | Plan full-book and volume rhythm into `memory/future/` |
| `/novel-plan` | Create chapter synopsis, outline, context, and optional HTML review files |
| `/novel-write` | Create plot points, style drafts, and merged `正文.md` |
| `/novel-revise` | Process marked prose revisions one span at a time |
| `/novel-sync` | Update `past.md`, future trackers, entities, graph, and project progress |
| `/novel-name` | Generate Chinese-style names |
| `/novel-progress` | Generate local progress chart |
| `/novel-snapshot` | Create or restore project snapshots |

## Project Layout

The Codex Skill expects or creates this local novel project structure:

```text
your-novel/
├── CLAUDE.md
├── memory/
│   ├── _graph.json
│   ├── _index.json
│   ├── entities/
│   ├── past.md
│   └── future/
├── chapters/
│   └── vol-01/
│       └── ch-0001/
├── templates/
└── .snapshots/
```

`CLAUDE.md` is treated as the project constitution. `memory/` stores durable story state. `chapters/` stores per-chapter artifacts.

## Bundled Tools

The skill includes helper scripts under `codex/skills/vibe-noveling/scripts/`:

- `init_project.py` - initialize a local novel project
- `knowledge_graph.py` - search, create, and rebuild entity indexes
- `namegen/name_generator.py` - generate character, faction, item, technique, location, creature, alchemy, and dao names
- `progress_chart.py` - generate `progress.html`
- `snapshot.py` - create/list/restore snapshots
- `word_counter.py` - count chapter words

Prefer `--project-root <path>` when a script supports it, or set:

```powershell
$env:VIBE_NOVEL_PROJECT_ROOT="D:\path\to\your-novel"
```

## Quick Start

```text
用 $vibe-noveling 初始化一个都市小说项目，书名《一个失业的39岁程序员》
```

Then:

```text
用 $vibe-noveling 帮我设计主角、核心困境和第一卷爽点
```

Then:

```text
用 $vibe-noveling 规划第一章，并在确认后写正文
```

## Validation

To validate the Codex Skill metadata locally:

```powershell
$env:PYTHONUTF8="1"
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" .\codex\skills\vibe-noveling
```

## Notes

- The Codex adapter does not remove or replace the Claude Code plugin.
- The Claude Code plugin remains under `plugins/vibe-noveling/`.
- The adapter reuses upstream workflow concepts, references, templates, and scripts, but routes them through Codex Skill semantics.
