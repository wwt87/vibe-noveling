# 讨论设定与剧情方向

Use when the user wants to discuss worldbuilding, characters, factions, items, systems, future plot direction, or story problems before formal planning.

## Context Routing

Read `CLAUDE.md` first. Then load only the needed reference:

- World design: `world-design.md`
- Character design: `character.md`
- Faction design: `faction-design.md`
- Item design: `item-design.md`
- Concept/system design: `concept-design.md`
- Event/future direction: `event-canvas.md`
- Context boundaries: `context-routing.md`

Read the smallest relevant project context:

- `memory/worldbuilding.md` for world-level questions.
- Matching `memory/entities/**/<name>.md` files for known entities.
- `memory/future/` files for future plot direction.
- `memory/setting-todo.md` for unresolved setup.

## Conversation Pattern

- Use Socratic discussion for vague ideas, but become decisive when enough constraints are known.
- Convert confirmed decisions into durable files. Keep unconfirmed alternatives in the conversation or `setting-todo.md`.
- For future plot direction, finish with 5W1H before writing to `memory/future/40-events/` or `20-threads.md`.

## Knowledge Graph

For entity search or rebuild:

```bash
python <skill>/scripts/knowledge_graph.py --project-root <project> search <query>
python <skill>/scripts/knowledge_graph.py --project-root <project> update character <name>
python <skill>/scripts/knowledge_graph.py --project-root <project> rebuild
```

Edit entity `.md` files directly, then rebuild. Do not hand-edit `_graph.json` or `_index.json`.

## Optional Branches

Load `upstream/booming.md` when the user says the plot is too flat, not explosive enough, or wants to "掀桌". Produce high-impact directions, then feed the selected one back into discussion or chapter planning.

Load `upstream/fuck-it.md` when the chapter endpoint should stay fixed but the internal path needs more drama, pressure, or comic-book exaggeration. Use it during discussion or chapter planning.
