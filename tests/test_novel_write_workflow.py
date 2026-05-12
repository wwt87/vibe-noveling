import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = (ROOT / "README.md").read_text()
WRITER_ZHOUZI = (ROOT / "plugins/vibe-noveling/agents/writer-zhouzi.md").read_text()
WRITER_DAZHONGMA = (ROOT / "plugins/vibe-noveling/agents/writer-dazhongma.md").read_text()
PLAN_SKILL = (ROOT / "plugins/vibe-noveling/skills/novel-plan/SKILL.md").read_text()
PLAN_OUTPUT = (ROOT / "plugins/vibe-noveling/skills/novel-plan/references/output.md").read_text()


class NovelWriteWorkflowTests(unittest.TestCase):
    def test_readme_no_longer_mentions_write_stage_ssot_for_writers(self):
        self.assertNotIn("writer 先用 SSoT 为 20 个剧情点做章内分布规划", README)
        self.assertNotIn("writer 在章内用 SSoT 先做分布规划", README)

    def test_writer_agents_no_longer_embed_write_stage_ssot_contract(self):
        for content in (WRITER_ZHOUZI, WRITER_DAZHONGMA):
            self.assertNotIn("SSoT 章内防趋同执行规约", content)
            self.assertNotIn("四层分布规划", content)
            self.assertNotIn("先分桶，再写作", content)

    def test_plan_viewer_templates_exist(self):
        synopsis = ROOT / "plugins/vibe-noveling/skills/novel-plan/templates/synopsis-viewer.html"
        outline = ROOT / "plugins/vibe-noveling/skills/novel-plan/templates/outline-viewer.html"
        self.assertTrue(synopsis.exists(), "synopsis-viewer.html 模板文件缺失")
        self.assertTrue(outline.exists(), "outline-viewer.html 模板文件缺失")

    def test_skill_md_mentions_html_visualization(self):
        self.assertIn("synopsis-viewer.html", PLAN_SKILL)
        self.assertIn("outline-viewer.html", PLAN_SKILL)
        self.assertIn("synopsis-view.html", PLAN_SKILL)
        self.assertIn("outline-view.html", PLAN_SKILL)

    def test_output_md_mentions_html_generation(self):
        self.assertIn("HTML 可视化生成", PLAN_OUTPUT)
        self.assertIn("synopsis-viewer.html", PLAN_OUTPUT)
        self.assertIn("outline-viewer.html", PLAN_OUTPUT)


if __name__ == "__main__":
    unittest.main()
