## 2024-05-24 - Informative illustrations require descriptive alt text
**Learning:** In a repository primarily focused on documentation and organization profiles, the primary UX interactions are visual. Informative illustrations, such as the organization mascot, serve as key brand identifiers and should be accessible to screen reader users via descriptive alt text rather than being treated as purely decorative.
**Action:** Always check `<img>` tags in Markdown files for missing or empty `alt` attributes and provide meaningful descriptions that convey the purpose or content of the image.

## 2026-04-02 - Use semantic alert blocks for critical documentation disclaimers
**Learning:** Plain-text disclaimers in documentation can be easily overlooked. Converting these to semantic GitHub-native alert blocks (e.g., `> [!IMPORTANT]`) significantly improves visual hierarchy, scannability, and ensures that critical context is immediately apparent to all users, including those using assistive technologies.
**Action:** Identify plain-text call-to-actions or disclaimers in Markdown files and wrap them in the appropriate semantic alert block to enhance visibility and accessibility.

## 2026-05-27 - Enhance critical security instructions with alert blocks and mailto links
**Learning:** Security reporting instructions are high-priority but can be overlooked in plain Markdown. Using a `> [!WARNING]` alert block improves visual hierarchy and urgency. Furthermore, providing a direct `mailto:` link for security email addresses reduces friction for reporters, making the process more accessible and intuitive.
**Action:** In `SECURITY.md` or similar sensitive files, wrap critical reporting instructions in a prominent alert block and ensure email addresses are interactive via `mailto:` links.

## 2026-06-15 - Improve support documentation scannability with semantic alert blocks
**Learning:** Support documentation often contains multiple call-to-actions, such as community forums and maintenance statements. Wrapping these in semantic alert blocks (e.g., `> [!TIP]` for helpful links and `> [!NOTE]` for project status) improves scannability and ensures users can quickly find the help they need.
**Action:** Use appropriate semantic alert blocks to distinguish between different types of support resources and project information in `SUPPORT.md`.

## 2026-07-20 - Highlight regulatory and compliance notices in contribution guidelines
**Learning:** Contributor guidelines must clearly surface important administrative requirements, such as adherence to the Code of Conduct. Using a prominent `> [!IMPORTANT]` alert block instead of plain body text significantly improves user awareness and ensures compliance boundaries are highly scannable before any contributions are initiated.
**Action:** Identify critical policy or compliance statements in contribution guides and wrap them in standard alert blocks to guarantee visibility.
