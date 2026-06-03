## 2024-05-24 - Informative illustrations require descriptive alt text
**Learning:** In a repository primarily focused on documentation and organization profiles, the primary UX interactions are visual. Informative illustrations, such as the organization mascot, serve as key brand identifiers and should be accessible to screen reader users via descriptive alt text rather than being treated as purely decorative.
**Action:** Always check `<img>` tags in Markdown files for missing or empty `alt` attributes and provide meaningful descriptions that convey the purpose or content of the image.

## 2026-04-02 - Use semantic alert blocks for critical documentation disclaimers
**Learning:** Plain-text disclaimers in documentation can be easily overlooked. Converting these to semantic GitHub-native alert blocks (e.g., `> [!IMPORTANT]`) significantly improves visual hierarchy, scannability, and ensures that critical context is immediately apparent to all users, including those using assistive technologies.
**Action:** Identify plain-text call-to-actions or disclaimers in Markdown files and wrap them in the appropriate semantic alert block to enhance visibility and accessibility.

## 2026-05-27 - Enhance critical security instructions with alert blocks and mailto links
**Learning:** Security reporting instructions are high-priority but can be overlooked in plain Markdown. Using a `> [!WARNING]` alert block improves visual hierarchy and urgency. Furthermore, providing a direct `mailto:` link for security email addresses reduces friction for reporters, making the process more accessible and intuitive.
**Action:** In `SECURITY.md` or similar sensitive files, wrap critical reporting instructions in a prominent alert block and ensure email addresses are interactive via `mailto:` links.

## 2026-06-12 - Actionable reporting instructions reduce friction in Code of Conduct
**Learning:** Placeholder text in Code of Conduct files (like `[INSERT CONTACT METHOD]`) creates significant friction and uncertainty for potential reporters. Replacing these placeholders with direct, interactive contact methods such as `mailto:` links, especially when highlighted with `> [!IMPORTANT]` alert blocks, ensures that reporting instructions are immediately actionable, visually prominent, and accessible to all users.
**Action:** Always identify and replace placeholders in community governance documents with specific, interactive contact details and use semantic alert blocks to ensure they are the most visible part of the enforcement section.
