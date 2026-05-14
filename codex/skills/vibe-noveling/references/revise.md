# 正文返修

Use when the user has marked `正文.md` and asks to revise, process notes, polish selected lines, shorten, expand, or run `/novel-revise` semantics.

## Markup

- `**text**`: expand this passage.
- `~~text~~`: shorten/compress this passage.
- `*text*`: polish or smooth this passage.

Load `revision-rules.md` for detailed candidate-generation rules.

## Workflow

1. Read the target `正文.md`, `大纲.md`, and relevant `CLAUDE.md` constraints.
2. Find all marked spans in document order.
3. For each span, generate 3 distinct candidate rewrites grounded in the current chapter facts and style.
4. Present one span at a time and ask the user to choose, edit, skip, or provide custom text.
5. Apply the selected replacement immediately with `apply_patch`.
6. Continue until no marks remain.
7. Recommend sync only after the user confirms the final text.

## Guardrails

- Do not silently process all spans without user choice.
- Preserve surrounding paragraph rhythm unless the user asks for larger surgery.
- Do not change plot facts or chapter endpoint during local line revision.
- Remove markup around replaced passages.
