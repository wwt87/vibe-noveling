---
name: vibe-noveling
description: Local Chinese web novel creation workflow adapted from TulanCN/vibe-noveling for Codex. Use when the user wants to initialize a novel project, discuss worldbuilding or plot, plan a full book or volume, plan/revise a chapter outline, draft chapter prose, revise marked prose, sync memory/knowledge graph, generate Chinese fantasy names, create snapshots, view progress, or asks for /novel-init, /novel-discuss, /novel-bookplan, /novel-plan, /novel-write, /novel-revise, /novel-sync, /novel-name, /novel-snapshot, /novel-progress semantics outside Claude Code.
---

# Vibe Noveling For Codex

Use this skill to run the Vibe Noveling workflow as local files and scripts instead of Claude Code slash commands. Treat the active novel project as the current working directory unless the user names another path.

## Route By Intent

- Initialize/new project, `/novel-init`: read `references/init.md`.
- Discuss settings, characters, worldbuilding, future direction, `/novel-discuss`: read `references/discuss.md`.
- Full-book or volume structure, `/novel-bookplan`: read `references/bookplan.md`.
- Plan or revise a chapter, `/novel-plan`: read `references/plan.md`.
- Write chapter prose, `/novel-write`: read `references/write.md`.
- Revise marked prose, `/novel-revise`: read `references/revise.md`.
- Sync completed chapter state, `/novel-sync`: read `references/sync.md`.
- Generate names, progress, snapshots, knowledge graph commands: read `references/tools.md`.
- Plot too flat / "booming": additionally read `references/upstream/booming.md`.
- Same endpoint but more dramatic / "fuck-it": additionally read `references/upstream/fuck-it.md`.

Load only the relevant reference files. For detailed style checks, load `ai-smell-checklist.md` only when planning/writing quality checks require it.

## Local Project Contract

Expected project shape:

```text
CLAUDE.md
memory/
  entities/{characters,locations,factions,items,concepts,systems}/
  past.md
  future/
chapters/vol-xx/ch-yyyy/
templates/
.snapshots/
```

`CLAUDE.md` is the project constitution. Use it before planning or writing. `memory/` is durable state. `chapters/` contains chapter artifacts.

## Command Mapping

The original slash commands are not executable in Codex. Interpret them as workflow requests:

| User says | Do locally |
| --- | --- |
| `/novel-init` | Run `scripts/init_project.py`, then refine `CLAUDE.md` |
| `/novel-discuss` | Discuss, then write confirmed decisions to `memory/` |
| `/novel-bookplan` | Write full-book/volume plans into `memory/future/` |
| `/novel-plan` | Produce confirmed `故事梗概.md`, `大纲.md`, optional HTML review files |
| `/novel-write` | Produce `剧情点.md`, two style drafts, merged `正文.md` |
| `/novel-revise` | Process Markdown marks in `正文.md` one at a time |
| `/novel-sync` | Update `past.md`, future trackers, entities, graph, progress |
| `/novel-name` | Run or emulate the name generator |
| `/novel-progress` | Run `scripts/progress_chart.py` |
| `/novel-snapshot` | Run `scripts/snapshot.py` |

## Operating Rules

- Make changes when the user's intent is implementation, but ask one focused question if title/genre/chapter target is impossible to infer.
- Confirm before writing final chapter outlines, restoring snapshots, or syncing an unapproved draft.
- Use `apply_patch` for manual edits. Use scripts for deterministic tasks.
- Preserve existing project files and user edits. Do not overwrite old content unless the workflow explicitly calls for an update.
- Keep context bounded: after reading `memory/past.md`, do not recursively open every entity it mentions.
- Do not invent critical settings. Create placeholders or ask for the missing decision.
- If writing exposes a structural problem, return to chapter planning rather than hiding it in prose.

## Script Paths

Scripts live inside this skill:

- `scripts/init_project.py`
- `scripts/knowledge_graph.py`
- `scripts/progress_chart.py`
- `scripts/snapshot.py`
- `scripts/namegen/name_generator.py`
- `scripts/word_counter.py`

Use `--project-root <path>` when available, or set `VIBE_NOVEL_PROJECT_ROOT=<path>`.

## Attribution

This skill adapts the public MIT-licensed `TulanCN/vibe-noveling` Claude Code plugin into a local Codex workflow while keeping the original workflow concepts, references, templates, and helper scripts available as bundled resources.
