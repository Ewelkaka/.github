## 2024-05-24 - Informative illustrations require descriptive alt text
**Learning:** In a repository primarily focused on documentation and organization profiles, the primary UX interactions are visual. Informative illustrations, such as the organization mascot, serve as key brand identifiers and should be accessible to screen reader users via descriptive alt text rather than being treated as purely decorative.
**Action:** Always check `<img>` tags in Markdown files for missing or empty `alt` attributes and provide meaningful descriptions that convey the purpose or content of the image.

## 2026-03-29 - Use GitHub-native alert blocks for critical project disclaimers
**Learning:** In text-heavy repositories, critical project disclaimers can easily be missed. GitHub-native alert blocks (e.g., `> [!NOTE]`) provide a standardized, visually distinct way to highlight this information, improving both accessibility and information hierarchy.
**Action:** Identify key disclaimers or instructions in documentation and wrap them in semantic alert blocks to ensure they stand out to readers.
