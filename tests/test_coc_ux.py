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
