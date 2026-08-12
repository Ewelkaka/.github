import os
import unittest
import re

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COC_PATH = os.path.join(REPO_ROOT, "CODE_OF_CONDUCT.md")

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COC_PATH = os.path.join(REPO_ROOT, "CODE_OF_CONDUCT.md")
README_PATH = os.path.join(REPO_ROOT, "README.md")

class TestCoCUX(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(COC_PATH, "r", encoding="utf-8") as f:
            cls.content = f.read()

    def test_reporting_contact_updated(self):
        self.assertIn("[opensource-security@github.com](mailto:opensource-security@github.com)", self.content)
        self.assertNotIn("[INSERT CONTACT METHOD]", self.content)

    def test_enforcement_alert_block(self):
        # Check for the alert block around the reporting section
        self.assertRegex(self.content, r"> \[!IMPORTANT\]\n> Instances of abusive")

    def test_mailto_link_accessibility(self):
        # Ensure mailto link is used for better UX
        self.assertIn("mailto:opensource-security@github.com", self.content)

if __name__ == "__main__":
    unittest.main()
            cls.coc_content = f.read()
        with open(README_PATH, "r", encoding="utf-8") as f:
            cls.readme_content = f.read()

    def test_coc_alert_block_present(self):
        self.assertIn("> [!IMPORTANT]", self.coc_content)

    def test_coc_mailto_link_present(self):
        self.assertIn("[opensource-security@github.com](mailto:opensource-security@github.com)", self.coc_content)

    def test_readme_local_coc_link(self):
        self.assertIn("[Code of Conduct](CODE_OF_CONDUCT.md)", self.readme_content)

if __name__ == "__main__":
    unittest.main()

class TestCoCUX(unittest.TestCase):
    def setUp(self):
        with open(COC_PATH, "r", encoding="utf-8") as f:
            self.content = f.read()

    def test_enforcement_alert_block(self):
        self.assertIn("> [!IMPORTANT]", self.content)
        self.assertIn("Instances of abusive, harassing, or otherwise unacceptable behavior", self.content)

    def test_reporting_email_link(self):
        self.assertIn("[opensource-security@github.com](mailto:opensource-security@github.com)", self.content)

if __name__ == "__main__":
    unittest.main()
README_PATH = os.path.join(REPO_ROOT, "README.md")
COC_PATH = os.path.join(REPO_ROOT, "CODE_OF_CONDUCT.md")
CONTRIBUTING_PATH = os.path.join(REPO_ROOT, "CONTRIBUTING.md")

class TestCoCUX(unittest.TestCase):
    def test_readme_local_coc_link(self):
        with open(README_PATH, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("[Code of Conduct](CODE_OF_CONDUCT.md)", content)
        self.assertNotIn("https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md", content)

    def test_coc_reporting_instructions(self):
        with open(COC_PATH, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertNotIn("[INSERT CONTACT METHOD]", content)
        self.assertIn("> [!IMPORTANT]", content)
        self.assertIn("opensource-security@github.com", content)
        self.assertIn("mailto:opensource-security@github.com", content)

    def test_contributing_coc_link(self):
        with open(CONTRIBUTING_PATH, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("[Code of Conduct](CODE_OF_CONDUCT.md)", content)

if __name__ == "__main__":
    unittest.main()
CONTRIBUTING_PATH = os.path.join(REPO_ROOT, "CONTRIBUTING.md")
COC_PATH = os.path.join(REPO_ROOT, "CODE_OF_CONDUCT.md")

class TestCoCUX(unittest.TestCase):
    def test_coc_placeholder_removed(self):
        with open(COC_PATH, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertNotIn("[INSERT CONTACT METHOD]", content)
        self.assertIn("opensource-security@github.com", content)
        self.assertIn("mailto:opensource-security@github.com", content)

    def test_readme_coc_link_localized(self):
        with open(README_PATH, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("[Code of Conduct](CODE_OF_CONDUCT.md)", content)
        self.assertNotIn("https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md", content)

    def test_contributing_coc_link_added(self):
        with open(CONTRIBUTING_PATH, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("[Contributor Code of Conduct](CODE_OF_CONDUCT.md)", content)

if __name__ == "__main__":
    unittest.main()
import unittest, os

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class TestCoCUX(unittest.TestCase):
    def test_ux_improvements(self):
        # SUPPORT.md typo
        with open(os.path.join(R, "SUPPORT.md")) as f:
            self.assertIn("feature request", f.read())
        # CODE_OF_CONDUCT.md reporting & alert
        with open(os.path.join(R, "CODE_OF_CONDUCT.md")) as f:
            c = f.read()
            self.assertIn("> [!IMPORTANT]", c)
            self.assertIn("opensource-security@github.com", c)
        # README.md local link
        with open(os.path.join(R, "README.md")) as f:
            self.assertIn("[Code of Conduct](CODE_OF_CONDUCT.md)", f.read())
        # CONTRIBUTING.md local link
        with open(os.path.join(R, "CONTRIBUTING.md")) as f:
            self.assertIn("[Code of Conduct](CODE_OF_CONDUCT.md)", f.read())
