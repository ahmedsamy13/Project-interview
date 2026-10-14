"""Exercise broken distributables, not mentoring prose or heading choices."""

from pathlib import Path
import shutil
import tempfile
import unittest

from tools.validate_skill import ROOT, validate


class PackageValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.skill = Path(self.temp.name) / "project-interview"
        shutil.copytree(ROOT / "skills" / "project-interview", self.skill)

    def test_distributable_is_self_contained(self):
        self.assertEqual(validate(self.skill), [])

    def test_missing_reference_is_rejected(self):
        (self.skill / "references" / "memory.md").unlink()
        self.assertTrue(any("Broken local link" in error for error in validate(self.skill)))

    def test_resource_cannot_escape_installation(self):
        entry = self.skill / "SKILL.md"
        entry.write_text(entry.read_text(encoding="utf-8") + "\n[external](../private.md)\n", encoding="utf-8")
        self.assertTrue(any("Link escapes skill" in error for error in validate(self.skill)))

    def test_unreachable_reference_is_rejected(self):
        (self.skill / "references" / "unused.md").write_text("Unreachable guidance\n", encoding="utf-8")
        self.assertTrue(any("not discoverable" in error for error in validate(self.skill)))

    def test_invalid_yaml_is_rejected_without_crashing(self):
        (self.skill / "agents" / "openai.yaml").write_text("interface: [broken\n", encoding="utf-8")
        self.assertTrue(any("Invalid YAML" in error for error in validate(self.skill)))

    def test_wrong_invocation_is_rejected(self):
        path = self.skill / "agents" / "openai.yaml"
        path.write_text(path.read_text(encoding="utf-8").replace("$project-interview", "$missing"), encoding="utf-8")
        self.assertTrue(any("invocation" in error for error in validate(self.skill)))

    def test_placeholders_are_allowed_only_in_output_templates(self):
        entry = self.skill / "SKILL.md"
        entry.write_text(entry.read_text(encoding="utf-8") + "\n{{unfinished}}\n", encoding="utf-8")
        self.assertTrue(any("Unfilled template" in error for error in validate(self.skill)))

    def test_missing_frontmatter_is_rejected(self):
        (self.skill / "SKILL.md").write_text("# Missing metadata\n", encoding="utf-8")
        self.assertTrue(any("frontmatter" in error for error in validate(self.skill)))


if __name__ == "__main__":
    unittest.main()
