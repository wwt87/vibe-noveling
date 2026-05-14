# 单章规划

Use when the user asks to plan the next chapter, revise an outline, adjust chapter structure, or run `/novel-plan` semantics locally.

## Read Before Planning

Read `CLAUDE.md`. Then gather bounded context:

1. Current event file in `memory/future/40-events/` if known.
2. Relevant entity files found by `knowledge_graph.py search`.
3. `memory/future/20-threads.md` and `90-sync-tracker.md`.
4. Previous chapter `chapters/vol-xx/ch-yyyy/正文.md`.
5. `memory/past.md`, then stop. Do not recursively expand every entity mentioned in `past.md`.

If volume or event context is missing and the chapter depends on it, ask for the smallest missing decision or suggest returning to book planning.

## Three Root Questions

Before writing the outline, answer internally:

1. Why must this chapter exist?
2. What concrete state change happens from beginning to end?
3. How does the protagonist actively drive the situation?

If these cannot be answered from context, stop and ask one focused question with 2-3 options.

## Output Flow

1. Identify volume, chapter number, chapter duty, what this chapter does not handle, and density.
2. Produce a chapter task card: main task, must-advance lines, deferrable lines, suggested ending point.
3. Fix starting state from previous actual text and ending goal from future/event/thread duties.
4. Draft a 3-8 paragraph story synopsis as a causal chain, not a list.
5. Clarify only the unclear bridge/motivation/reveal point; ask one question at a time.
6. Produce a two-layer outline:
   - `剧情思路卡`: core payoff, protagonist state change, conflict chain, information-release strategy, chapter boundary.
   - `可写场景纲要`: 3-6 narrative scene blocks. Each block title: `### 场景 N：名称 | 密度：高/中/低`.
7. Run outline smell checks from `planning-checks.md`. Rewrite any scene block that triggers 3+ issues.
8. Confirm title separately. Use `待定` if not decided.

## Files

Write only after the user confirms the content:

```text
chapters/vol-xx/ch-yyyy/
├── 故事梗概.md
├── 大纲.md
├── 上下文.md
├── synopsis-view.html
└── outline-view.html
```

Use `assets/templates/synopsis-viewer.html` and `assets/templates/outline-viewer.html` if generating editable HTML review pages. If a browser cannot be opened, still write the HTML and give the local path.

## Revision Mode

If `大纲.md` exists or the user says "在原大纲上改":

- Read existing outline.
- Summarize keep/change/delete boundaries.
- Offer 2-3 revision strategies.
- Modify only affected sections unless the structure is broken.

## Guardrails

- Do not save unconfirmed outline text.
- Do not add dialogue/style prose into the outline; that belongs to writing.
- Do not change chapter endpoint inside `fuck-it`; load `upstream/fuck-it.md` for same-endpoint strengthening.
- If the plan requires reordering major beats, return to revision mode instead of hiding the change inside prose.
