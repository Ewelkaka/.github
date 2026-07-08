# Bolt's Journal - Critical Learnings Only
## 2026-07-08 - Avoiding bytecode pollution in PRs
**Learning:** Running Python tests locally generates __pycache__ directories and .pyc files, which can accidentally be included in the PR if .gitignore is not properly configured. This was flagged during code review.
**Action:** Always include Python bytecode patterns in .gitignore and run a cleanup command (find . -name "__pycache__" -type d -exec rm -rf {} +) before staging changes for a PR.
