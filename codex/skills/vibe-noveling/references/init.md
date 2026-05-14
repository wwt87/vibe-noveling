# 初始化本地小说项目

Use when the user wants to initialize, create, or bootstrap a novel project.

## Workflow

1. Confirm only the missing essentials: title and genre. If the user already supplied them, do not ask again.
2. Run:

```bash
python <skill>/scripts/init_project.py <project-root> --title "<书名>" --genre "<类型>"
```

3. Open `CLAUDE.md` and fill any extra "小说宪法" fields the user has already provided. If a field is unknown, leave `待定`; do not invent it.
4. Tell the user the next best step is usually world/character discussion, then book planning, then chapter planning.

## Project Skeleton

The initializer creates:

- `CLAUDE.md`
- `memory/_graph.json`, `memory/_index.json`
- `memory/entities/{characters,locations,factions,items,concepts,systems}/`
- `memory/worldbuilding.md`, `memory/world-design-progress.md`, `memory/setting-todo.md`, `memory/past.md`
- `memory/future/{00-index,10-book,20-threads,90-sync-tracker}.md`
- `memory/future/{30-volumes,40-events}/`
- `chapters/vol-01/ch-0001/`
- `templates/`
- `.snapshots/`

## Guardrails

- Preserve existing files. The script only writes missing files.
- Do not force the original README's male-frequency default if the user wants another genre or audience.
- Treat `CLAUDE.md` as the project constitution. Later planning and writing must obey it.
