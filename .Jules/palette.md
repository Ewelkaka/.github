## 2024-05-24 - Informative illustrations require descriptive alt text
**Learning:** In a repository primarily focused on documentation and organization profiles, the primary UX interactions are visual. Informative illustrations, such as the organization mascot, serve as key brand identifiers and should be accessible to screen reader users via descriptive alt text rather than being treated as purely decorative.
**Action:** Always check `<img>` tags in Markdown files for missing or empty `alt` attributes and provide meaningful descriptions that convey the purpose or content of the image.

## 2026-03-31 - Semantic Alert blocks improve scannability and accessibility
**Learning:** For repositories focused on GitHub-native documentation, using semantic Alert blocks (`> [!NOTE]`, `> [!TIP]`, etc.) instead of plain italicized text significantly improves content scannability and accessibility. These blocks are visually distinct and can be properly identified by screen readers, making critical information or tips stand out.
**Action:** Replace italicized or plain text introductions/notes with the appropriate GitHub-flavored Markdown Alert blocks to enhance user experience and clarity.
