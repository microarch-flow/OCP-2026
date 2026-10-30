"""Regression tests: python knowledge/scripts/test_table_wikilinks.py."""
from contextlib import redirect_stdout
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from table_wikilinks import find_unescaped_table_aliases, normalize_table_aliases


class TableWikiLinksTest(unittest.TestCase):
    def test_only_alias_pipes_change(self):
        old = "| Name | Evidence |\n|---|---|\n| 中文 | [[目录/原件.pdf#page=3|PDF p.3]] |\n"
        new = old.replace("#page=3|", "#page=3\\|")
        self.assertEqual(normalize_table_aliases(old), new)
        issue, = find_unescaped_table_aliases(old)
        self.assertEqual(issue.line, 3)
        self.assertEqual(old[issue.offset], "|")

    def test_existing_escapes_and_idempotence(self):
        old = "| Name | Evidence |\n|---|---|\n| [[a\\|A]] | [[b|B]] ![[c|C]] |\n"
        new = normalize_table_aliases(old)
        self.assertIn("[[a\\|A]]", new)
        self.assertIn("[[b\\|B]] ![[c\\|C]]", new)
        self.assertEqual(normalize_table_aliases(new), new)
        self.assertEqual(find_unescaped_table_aliases(new), [])

    def test_prose_and_non_table_pipe_lines_unchanged(self):
        text = "[[a|A]]\n| [[b|B]] | no delimiter |\n\nOther prose.\n"
        self.assertEqual(normalize_table_aliases(text), text)

    def test_frontmatter_and_code_preserved(self):
        example = "| Header |\n|---|\n| [[example|Example]] |\n"
        protected = ("---\nexample: |\n" + example + "---\n\n"
                     + "```markdown\n" + example + "```\n\n"
                     + "~~~~md\n" + example + "~~~\n" + example + "~~~~\n\n"
                     + "    | Header |\n    |---|\n    | [[example|Example]] |\n")
        self.assertEqual(normalize_table_aliases(protected), protected)

    def test_inline_code_and_escaped_openers_preserved(self):
        text = "| H |\n|---|\n| `[[code|C]]` ``[[also-code|D]]`` \\[[escaped|E]] [[real|R]] |\n"
        expected = text.replace("[[real|R]]", "[[real\\|R]]")
        self.assertEqual(normalize_table_aliases(text), expected)

    def test_optional_outer_pipes_and_header_alias(self):
        text = "[[a|A]] | B\n:--- | ---:\n[[b|B]] | C\n\n[[outside|O]]\n"
        expected = text.replace("[[a|A]]", "[[a\\|A]]").replace("[[b|B]]", "[[b\\|B]]")
        self.assertEqual(normalize_table_aliases(text), expected)

    def test_crlf_unicode_bytes_preserved(self):
        text = "| 中文 |\r\n|---|\r\n| [[中文/路径|名]] |\r\n"
        expected = text.replace("路径|", "路径\\|")
        self.assertEqual(normalize_table_aliases(text).encode(), expected.encode())

    def test_comments_and_unclosed_fences_preserved(self):
        example = "| H |\n|---|\n| [[a|A]] |\n"
        text = "<!--\n" + example + "-->\n```md\n" + example
        self.assertEqual(normalize_table_aliases(text), text)

    def test_backslash_parity_and_multiple_alias_pipes(self):
        text = "| H |\n|---|\n| [[a\\\\|A|extra]] |\n"
        expected = text.replace("a\\\\|", "a\\\\\\|").replace("A|", "A\\|")
        self.assertEqual(normalize_table_aliases(text), expected)
        self.assertEqual(normalize_table_aliases(expected), expected)

    def test_malformed_or_no_alias_links_unchanged(self):
        text = "| H |\n|---|\n| [[no-alias]] [[|empty-target]] [[broken| [[nested|x]]]] |\n"
        self.assertEqual(normalize_table_aliases(text), text)

    def test_validator_fails_then_passes_after_normalization(self):
        import validate
        with tempfile.TemporaryDirectory() as directory:
            vault = Path(directory)
            knowledge = vault / "knowledge"
            (knowledge / "sources").mkdir(parents=True)
            note = knowledge / "note.md"
            note.write_text("| H |\n|---|\n| [[knowledge/note|self]] |\n", encoding="utf-8")
            (knowledge / "coverage.json").write_text(json.dumps({
                "pdf_total": 0, "topic_total": 0, "analysis_cards": 0,
                "analyzed_sources": 0, "zero_byte_sources": 0,
            }), encoding="utf-8")
            manifest = {"sources": [], "source_commit": "test-fixture"}
            with patch.object(validate, "KNOWLEDGE", knowledge), patch.object(validate, "VAULT", vault), \
                    patch.object(validate, "load_manifest", return_value=manifest), patch("sys.argv", ["validate.py"]):
                out = io.StringIO()
                with redirect_stdout(out):
                    self.assertEqual(validate.main(), 1)
                report = json.loads(out.getvalue())
                self.assertEqual(report["unescaped_table_alias_pipes"], 1)
                self.assertIn("unescaped table wikilink", report["errors"][0])
                note.write_text(normalize_table_aliases(note.read_text()), encoding="utf-8")
                with redirect_stdout(io.StringIO()):
                    self.assertEqual(validate.main(), 0)


if __name__ == "__main__":
    unittest.main()
