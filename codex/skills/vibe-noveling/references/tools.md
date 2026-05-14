# Local Tools

Use these scripts from the skill folder. Prefer passing `--project-root <project>` or setting `VIBE_NOVEL_PROJECT_ROOT`.

## Initialize

```bash
python <skill>/scripts/init_project.py <project-root> --title "<书名>" --genre "<类型>"
```

## Knowledge Graph

```bash
python <skill>/scripts/knowledge_graph.py --project-root <project> search <query> [-t type] [-l limit] [-j]
python <skill>/scripts/knowledge_graph.py --project-root <project> update <type> <name> [-j]
python <skill>/scripts/knowledge_graph.py --project-root <project> relations <entity_id>
python <skill>/scripts/knowledge_graph.py --project-root <project> tags <tag>
python <skill>/scripts/knowledge_graph.py --project-root <project> rebuild
```

Requires PyYAML for robust frontmatter parsing:

```bash
python -m pip install pyyaml
```

## Name Generator

```bash
python <skill>/scripts/namegen/name_generator.py character --gender 男 --count 5
python <skill>/scripts/namegen/name_generator.py technique --element 火 --category attack --count 5
python <skill>/scripts/namegen/name_generator.py faction --count 5
python <skill>/scripts/namegen/name_generator.py item --count 5
python <skill>/scripts/namegen/name_generator.py location --count 5
python <skill>/scripts/namegen/name_generator.py creature --count 5
python <skill>/scripts/namegen/name_generator.py alchemy --count 5
python <skill>/scripts/namegen/name_generator.py dao --gender 女 --count 5
```

Set `VIBE_NOVEL_PROJECT_ROOT=<project>` to exclude existing entity names.

## Progress

```bash
python <skill>/scripts/progress_chart.py --project-root <project> --open false
```

Generates `progress.html` by default.

## Snapshot

```bash
$env:SNAPSHOT_PROJECT_ROOT="<project>"
python <skill>/scripts/snapshot.py create "描述"
python <skill>/scripts/snapshot.py list
python <skill>/scripts/snapshot.py restore "<快照名>"
```

Confirm before restore because it replaces current `memory/`, `chapters/`, and `events/` after auto-backup.

## Word Counter

```bash
python <skill>/scripts/word_counter.py <file-or-dir>
```

Use when checking chapter or draft length.
