#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


ENTITY_DIRS = ["characters", "locations", "factions", "items", "concepts", "systems"]


def write_if_missing(path: Path, content: str) -> bool:
    if path.exists():
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


def build_claude_md(title: str, genre: str) -> str:
    return f"""# CLAUDE.md

## 项目概述
- 书名：{title}
- 类型：{genre}

## 小说宪法
> 本小说创作的最高准则。剧情设计、详略讨论、正文合并均须服从。
> 讨论中可随时修正，修正后立即更新本节。

### 灵魂
待定

### 爽感公式
- 来源：待定
- 递进节奏：待定

### 叙事纹理
- 节奏倾向：待定
- 文字质感：待定
- 信息密度：待定

### 主角光谱
- 主角吸引力来源：待定
- 主角与读者的关系：待定

### 作者人格
- 叙事姿态：待定
- 价值底色：待定
- 情感温度：待定
- 幽默方式：待定
- 信息习惯：待定

### 绝对红线
- 待定

### 风格锚点
- 待定

## 创作进度
- 当前卷：Vol-01
- 当前章节：第 1 章（待规划）

## 目录结构说明
- `memory/`：长期记忆、设定实体、已完成剧情与未来规划
- `chapters/`：章节大纲、上下文、中间稿和正文
- `templates/`：项目级模板
- `.snapshots/`：快照备份

## 可用 Codex 工作流
- 初始化：使用 `$vibe-noveling` 的 init 流程或运行 `scripts/init_project.py`
- 讨论设定：按 `references/discuss.md` 和相关 reference 维护 `memory/`
- 全书规划：按 `references/bookplan.md` 写入 `memory/future/`
- 单章规划：按 `references/plan.md` 写入章节目录
- 正文创作：按 `references/write.md` 生成剧情点、中间稿和正文
- 返修同步：按 `references/revise.md`、`references/sync.md` 处理
"""


def main() -> None:
    parser = argparse.ArgumentParser(description="Initialize a local Vibe Noveling project for Codex.")
    parser.add_argument("project_root", nargs="?", default=".", help="小说项目根目录")
    parser.add_argument("--title", required=True, help="书名")
    parser.add_argument("--genre", default="待定", help="类型，例如 修真仙侠/玄幻奇幻/都市现代")
    args = parser.parse_args()

    root = Path(args.project_root).expanduser().resolve()
    created: list[str] = []

    dirs = [
        root / "memory" / "entities",
        root / "memory" / "future" / "30-volumes",
        root / "memory" / "future" / "40-events",
        root / "chapters" / "vol-01" / "ch-0001",
        root / "templates",
        root / ".snapshots",
    ]
    dirs.extend(root / "memory" / "entities" / name for name in ENTITY_DIRS)
    for directory in dirs:
        directory.mkdir(parents=True, exist_ok=True)

    files = {
        root / "CLAUDE.md": build_claude_md(args.title, args.genre),
        root / "memory" / "_graph.json": json.dumps({"version": "1.0", "entities": {}, "relations": []}, ensure_ascii=False, indent=2) + "\n",
        root / "memory" / "_index.json": json.dumps(
            {"version": "1.0", "name_index": {}, "tag_index": {}, "type_index": {}},
            ensure_ascii=False,
            indent=2,
        ) + "\n",
        root / "memory" / "entities" / "README.md": """# 实体文件规范

实体文件放在 `memory/entities/<type>/` 下，使用 YAML frontmatter：

```yaml
---
id: char_example
name: 示例
type: character
aliases: []
tags: []
relations: []
---
```
""",
        root / "memory" / "past.md": "# 已完成剧情\n\n尚无已完成章节。\n",
        root / "memory" / "worldbuilding.md": "# 世界观总览\n\n待定。\n",
        root / "memory" / "world-design-progress.md": """# 世界观构建进度

- [ ] 世界本质
- [ ] 能力体系
- [ ] 社会形态
- [ ] 势力格局
- [ ] 地理环境
- [ ] 历史背景
- [ ] 经济物品
- [ ] 核心矛盾
""",
        root / "memory" / "setting-todo.md": "# 设定待办\n\n",
        root / "memory" / "future" / "00-index.md": """# Future 索引

读取顺序：`10-book.md` → `20-threads.md` → `30-volumes/` → `40-events/` → `90-sync-tracker.md`。
""",
        root / "memory" / "future" / "10-book.md": "# 全书锚点\n\n待规划。\n",
        root / "memory" / "future" / "20-threads.md": "# 长期线程总表\n\n",
        root / "memory" / "future" / "90-sync-tracker.md": "# 同步追踪表\n\n",
        root / "templates" / "chapter-template.md": "# 第 X 章：待定\n\n## 故事梗概\n\n## 大纲\n\n## 正文\n",
        root / "templates" / "character-template.md": """---
id: char_
name:
type: character
aliases: []
tags: []
relations: []
---

# 角色名

## 基本信息

## 当前状态

## 关系
""",
    }

    for path, content in files.items():
        if write_if_missing(path, content):
            created.append(str(path.relative_to(root)))

    print(f"Vibe Noveling project initialized: {root}")
    if created:
        print("Created files:")
        for item in created:
            print(f"- {item}")
    else:
        print("No files overwritten; existing project skeleton kept.")


if __name__ == "__main__":
    main()
