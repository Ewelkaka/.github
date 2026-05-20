## 2024-05-24 - Informative illustrations require descriptive alt text
**Learning:** In a repository primarily focused on documentation and organization profiles, the primary UX interactions are visual. Informative illustrations, such as the organization mascot, serve as key brand identifiers and should be accessible to screen reader users via descriptive alt text rather than being treated as purely decorative.
**Action:** Always check `<img>` tags in Markdown files for missing or empty `alt` attributes and provide meaningful descriptions that convey the purpose or content of the image.

## 2026-04-02 - Use semantic alert blocks for critical documentation disclaimers
**Learning:** Plain-text disclaimers in documentation can be easily overlooked. Converting these to semantic GitHub-native alert blocks (e.g., `> [!IMPORTANT]`) significantly improves visual hierarchy, scannability, and ensures that critical context is immediately apparent to all users, including those using assistive technologies.
**Action:** Identify plain-text call-to-actions or disclaimers in Markdown files and wrap them in the appropriate semantic alert block to enhance visibility and accessibility.

## 2026-04-03 - Combine alert blocks with actionable links for critical paths
**Learning:** High-priority instructions, such as security reporting procedures, benefit from combining visual prominence (alert blocks) with direct actionability (mailto: links). This reduces cognitive load by clearly identifying the 'what' (warning) and providing an immediate 'how' (contact link) in a single scannable unit.
**Action:** When creating or updating critical documentation alerts, ensure that any associated contact methods or external resources are directly linked within the block to facilitate immediate user action.
