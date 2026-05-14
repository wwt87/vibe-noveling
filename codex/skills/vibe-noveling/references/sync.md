# 状态同步

Use after a chapter正文 is approved and the user asks to sync, update memory, update knowledge graph, or run `/novel-sync` semantics.

## Workflow

1. Confirm target volume/chapter and list files to update:
   - `memory/past.md`
   - `memory/future/20-threads.md`
   - `memory/future/90-sync-tracker.md`
   - relevant `memory/entities/**`
   - `CLAUDE.md` progress
2. Read `chapters/vol-xx/ch-yyyy/正文.md` and `大纲.md`.
3. Append a <=100 Chinese character summary of core events and state changes to `memory/past.md`.
4. Update thread states and sync tracker:
   - newly handed-off hooks go into `90-sync-tracker.md`
   - paid-off hooks are marked or removed after preserving history
5. Detect new or changed entities. Create files with:

```bash
python <skill>/scripts/knowledge_graph.py --project-root <project> update <type> <name>
```

6. Rebuild graph:

```bash
python <skill>/scripts/knowledge_graph.py --project-root <project> rebuild
```

7. Update `CLAUDE.md` current chapter progress.
8. Report changed files and unresolved follow-ups.

## Guardrails

- Never delete old `past.md` history.
- Do not put future plans in entity files. Future plans belong in `memory/future/`.
- Do not sync unapproved draft text.
