# Bolt Journal

## 2024-05-24 - Optimized test suite I/O
**Learning:** Redundant file I/O in test suites can be a significant source of overhead, especially when many tests read the same static files.
**Action:** Use @classmethod setUpClass to load static resources once per class instead of once per test method.
