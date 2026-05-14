# 正文创作

Use when the user asks to write, draft, expand, or run `/novel-write` semantics from an approved chapter outline.

## Required Context

1. `chapters/vol-xx/ch-yyyy/大纲.md`
2. `chapters/vol-xx/ch-yyyy/故事梗概.md` if present
3. `chapters/vol-xx/ch-yyyy/上下文.md` if present
4. Previous chapter `正文.md`
5. `memory/past.md`, then stop
6. Relevant entity files via `knowledge_graph.py search`
7. `memory/future/20-threads.md`, `90-sync-tracker.md`, and current event if relevant
8. `Opus报告.md` if present

If setting files are missing for critical entities, stop and either create placeholders with `knowledge_graph.py update` or ask for the missing setting.

## Process

1. Extract exactly 20 plot points from the narrative scene outline. Save `剧情点.md`.
2. If `Opus报告.md` says `需先重做大纲`, stop and route to planning revision. If it says `需小修后写`, save constraints to `写作约束.md`.
3. Read style references only when drafting:
   - `agents/writer-zhouzi.md` for fast modern conflict/action.
   - `agents/writer-dazhongma.md` for dramatic setups, reversals, and information-play.
4. Draft two full versions in order, each 2500-4000 Chinese characters by default, keeping headings like `【剧情点01：标题】`.
5. Save:
   - `会说话的肘子.md`
   - `大仲马.md`
6. Merge point by point. Each plot point picks one primary source; do not sentence-weave both versions. Remove plot-point headings in final prose. Save `正文.md`.
7. Run consistency pass: facts, names, time, viewpoint, chapter endpoint, and character voice.
8. Run AI-smell cleanup using `ai-smell-checklist.md`, then one independent polish pass.
9. Optionally use `word_counter.py` for counting or density support.

## Density

- High-density plot point: 200-400 chars, with sensory layer, present-character reaction, protagonist impact.
- Medium: 120-200 chars.
- Low: 50-100 chars, only action progression and information release.

## Guardrails

- Do not change the chapter endpoint or core chain during drafting.
- Do not invent critical missing setting.
- Do not keep plot-point headings in `正文.md`.
- If writing exposes a structural break, stop and route to `plan.md` revision.
- Final prose must be continuous Chinese fiction, not a report, outline, or writing note.
