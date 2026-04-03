## 2024-05-24 - Informative illustrations require descriptive alt text
**Learning:** In a repository primarily focused on documentation and organization profiles, the primary UX interactions are visual. Informative illustrations, such as the organization mascot, serve as key brand identifiers and should be accessible to screen reader users via descriptive alt text rather than being treated as purely decorative.
**Action:** Always check `<img>` tags in Markdown files for missing or empty `alt` attributes and provide meaningful descriptions that convey the purpose or content of the image.

## 2026-04-02 - Use semantic Alert blocks for key disclaimers
**Learning:** Critical information in documentation, such as disclaimers about what a repository is not, can be easily overlooked when presented as plain text or simple italics. GitHub-native Alert blocks (> [!IMPORTANT], > [!NOTE], etc.) provide significant visual prominence and semantic meaning, improving both scannability and accessibility.
**Action:** Identify critical call-to-actions or disclaimers in Markdown files and convert them to appropriate semantic Alert blocks to ensure they are noticed by users.
