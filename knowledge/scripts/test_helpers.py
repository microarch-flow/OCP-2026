"""Small standard-library regression tests; run with python knowledge/scripts/test_helpers.py."""
import hashlib
from pathlib import Path
import tempfile
import unittest

from common import generated, metadata, source_id, wiki_targets, wikilink


class HelpersTest(unittest.TestCase):
    def test_id_uses_exact_utf8_path(self):
        path = "Cooling：Cold Plate/一份资料.pdf"
        self.assertEqual(source_id(path), "src-" + hashlib.sha256(path.encode("utf-8")).hexdigest()[:12])
        self.assertNotEqual(source_id(path), source_id(path.replace("：", ":")))

    def test_table_link_keeps_original_path(self):
        path = "Cooling：Cold Plate/一份资料.pdf#page=3"
        link = wikilink(path, "PDF p.3", table=True)
        self.assertIn("\\|", link)
        self.assertEqual(list(wiki_targets(link)), [path])

    def test_code_examples_not_counted_as_actual_links(self):
        text = "`[[not-real]]`\n```md\n[[not-real-either]]\n```\n[[knowledge/index]]\n"
        self.assertEqual(list(wiki_targets(text)), ["knowledge/index"])

    def test_refresh_preserves_authored_text(self):
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / "topic.md"
            generated(path, "test", "old generated", "Authored introduction")
            with path.open("a", encoding="utf-8") as f:
                f.write("\nUser addition\n")
            generated(path, "test", "new generated", "Ignored new intro")
            text = path.read_text(encoding="utf-8")
            self.assertIn("Authored introduction", text)
            self.assertIn("User addition", text)
            self.assertIn("new generated", text)
            self.assertNotIn("old generated", text)

    def test_refresh_refuses_unmarked_existing_file(self):
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / "topic.md"
            path.write_text("User-owned file", encoding="utf-8")
            with self.assertRaises(ValueError):
                generated(path, "test", "replacement", "intro")

    def test_flat_metadata_preserves_links_and_unicode(self):
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / "card.md"
            path.write_text('---\nid: "src-example"\ntitle: "中文：Title"\nsource_pages: null\nevidence_pages: [1, 2]\nconcepts:\n  - "[[knowledge/concepts/example]]"\n---\n# Example\n', encoding="utf-8")
            data = metadata(path)
            self.assertEqual(data["source_pages"], None)
            self.assertEqual(data["evidence_pages"], [1, 2])
            self.assertEqual(data["concepts"], ["[[knowledge/concepts/example]]"])


if __name__ == "__main__":
    unittest.main()
