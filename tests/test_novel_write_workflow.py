import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = (ROOT / "README.md").read_text()
WRITER_ZHOUZI = (ROOT / "plugins/vibe-noveling/agents/writer-zhouzi.md").read_text()
WRITER_DAZHONGMA = (ROOT / "plugins/vibe-noveling/agents/writer-dazhongma.md").read_text()


class NovelWriteWorkflowTests(unittest.TestCase):
    def test_readme_no_longer_mentions_write_stage_ssot_for_writers(self):
        self.assertNotIn("writer 先用 SSoT 为 20 个剧情点做章内分布规划", README)
        self.assertNotIn("writer 在章内用 SSoT 先做分布规划", README)

    def test_writer_agents_no_longer_embed_write_stage_ssot_contract(self):
        for content in (WRITER_ZHOUZI, WRITER_DAZHONGMA):
            self.assertNotIn("SSoT 章内防趋同执行规约", content)
            self.assertNotIn("四层分布规划", content)
            self.assertNotIn("先分桶，再写作", content)


if __name__ == "__main__":
    unittest.main()
