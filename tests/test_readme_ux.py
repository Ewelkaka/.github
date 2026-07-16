import os
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README_PATH = os.path.join(REPO_ROOT, "README.md")

class TestReadmeUX(unittest.TestCase):
    def setUp(self):
        with open(README_PATH, "r", encoding="utf-8") as f:
            self.content = f.read()

    def test_alert_block_present(self):
        self.assertIn("> [!IMPORTANT]", self.content)
        self.assertIn("> This repository is not a course.", self.content)

    def test_descriptive_links(self):
        self.assertIn("[skills.github.com](https://skills.github.com)", self.content)
        self.assertIn("[organization profile](profile/README.md)", self.content)
        self.assertIn("[GitHub Skills content model](https://skills.github.com/content-model)", self.content)

    def test_copyright_year(self):
        self.assertIn("&copy; 2026 GitHub", self.content)

    def test_localized_links(self):
        self.assertIn("[Code of Conduct](CODE_OF_CONDUCT.md)", self.content)
        self.assertIn("[MIT License](LICENSE)", self.content)

    def test_external_coc_link_removed(self):
        """The old external contributor-covenant link must no longer be used."""
        self.assertNotIn("contributor-covenant.org", self.content)

    def test_external_license_shortlink_removed(self):
        """The old gh.io MIT license shortlink must no longer be used."""
        self.assertNotIn("gh.io/mit", self.content)

    def test_localized_link_targets_exist_on_disk(self):
        """Regression guard: local links in README.md must point to files that actually exist."""
        self.assertTrue(
            os.path.isfile(os.path.join(REPO_ROOT, "CODE_OF_CONDUCT.md")),
            "README.md links to CODE_OF_CONDUCT.md, but the file does not exist.",
        )
        self.assertTrue(
            os.path.isfile(os.path.join(REPO_ROOT, "LICENSE")),
            "README.md links to LICENSE, but the file does not exist.",
        )


class TestSupportUX(unittest.TestCase):
    def setUp(self):
        with open(os.path.join(REPO_ROOT, "SUPPORT.md"), "r", encoding="utf-8") as f:
            self.content = f.read()

    def test_typo_fix(self):
        self.assertIn("feature request", self.content)
        self.assertNotIn("feaure request", self.content)


class TestContributingUX(unittest.TestCase):
    def setUp(self):
        with open(os.path.join(REPO_ROOT, "CONTRIBUTING.md"), "r", encoding="utf-8") as f:
            self.content = f.read()

    def test_code_of_conduct_is_localized_link(self):
        """CONTRIBUTING.md must link to the local Code of Conduct file, not just mention it as plain text."""
        self.assertIn(
            "[Contributor Code of Conduct](CODE_OF_CONDUCT.md)",
            self.content,
        )

    def test_plain_text_reference_replaced(self):
        """The old unlinked plain-text reference must no longer be present verbatim."""
        self.assertNotIn(
            "released with a Contributor Code of Conduct. By participating",
            self.content,
        )

    def test_link_target_exists_on_disk(self):
        """Regression guard: the CODE_OF_CONDUCT.md link target must actually exist."""
        self.assertTrue(
            os.path.isfile(os.path.join(REPO_ROOT, "CODE_OF_CONDUCT.md")),
            "CONTRIBUTING.md links to CODE_OF_CONDUCT.md, but the file does not exist.",
        )


class TestGitignorePython(unittest.TestCase):
    def setUp(self):
        with open(os.path.join(REPO_ROOT, ".gitignore"), "r", encoding="utf-8") as f:
            self.content = f.read()

    def test_python_section_header_present(self):
        self.assertIn("# Python #", self.content)

    def test_pycache_ignored(self):
        self.assertIn("__pycache__/", self.content)

    def test_pyc_files_ignored(self):
        self.assertIn("*.pyc", self.content)

    def test_existing_os_section_preserved(self):
        """Pre-existing OS-generated file rules must remain untouched."""
        self.assertIn(".DS_Store", self.content)
        self.assertIn("Thumbs.db", self.content)


if __name__ == "__main__":
    unittest.main()
