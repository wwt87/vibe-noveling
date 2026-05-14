# 全书与分卷规划

Use when the user asks for 全书大纲, 卷结构, Save the Cat structure, long-term plot rhythm, or future-thread reorganization.

## Required Context

1. `CLAUDE.md`
2. `memory/future/00-index.md`, `10-book.md`, `20-threads.md`
3. Existing `memory/future/30-volumes/*.md`
4. Relevant setting files from `memory/`
5. Load `stc-story-types.md` and `stc-hierarchy.md` only when diagnosing or applying Save the Cat structure.

## Main Modes

- From zero: diagnose story type, produce one-sentence premise, expand into 5-act shape, then 15-beat full-book blueprint.
- Diagnose only: identify the 3 most likely story types and their promise/risk.
- Plan a volume: read full-book blueprint first; write `memory/future/30-volumes/vol-xx.md`.
- Replan after new setting: list impacts, preserve locked written content, propose minimal/medium/structural options.
- Manage `future/`: record ideas, merge duplicate hooks, update revision notes.

## Save Targets

```text
memory/future/
├── 10-book.md
├── 20-threads.md
├── 30-volumes/vol-xx.md
├── 40-events/<event>.md
└── 90-sync-tracker.md
```

## Guardrails

- Do not plan chapter-by-chapter here.
- Do not invent a full-book ending if the user has not approved the core promise.
- Do not overwrite locked beats or written-chapter facts without explicit approval.
- Prefer volume duties, state changes, and beat positions over fixed chapter counts.
