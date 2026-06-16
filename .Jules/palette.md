## 2026-06-16 - Duplicated Component Accessibility
**Learning:** In applications consisting of standalone static HTML files without a shared templating engine, accessibility issues like missing ARIA labels on common structural components (e.g., `#themeBtn`, modal close buttons) are systematically duplicated across all pages.
**Action:** When adding ARIA attributes to shared components in such architectures, use a script to batch search-and-replace across all HTML files to ensure consistency and prevent regressions in unedited files.
