# Bolt's Performance Journal

## 2026-04-10 - Redundant File I/O in Test Suite
**Learning:** The test suite was re-reading the same static Markdown files in every `setUp` method. For a small number of tests, this isn't a huge bottleneck, but it scales poorly. Moving file reading to `@classmethod setUpClass` reduces the number of `openat` calls from 19 to 3 for the current suite.
**Action:** Always check if tests are reading static assets in `setUp` and move them to `setUpClass` if the content doesn't change between tests.
