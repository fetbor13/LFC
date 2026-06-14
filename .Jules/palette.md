## 2024-06-14 - Aria Label on Theme Toggles
**Learning:** Because the application relies on many standalone static HTML files, global UI elements like the theme toggle button (`#themeBtn`) are repeated across nearly every page. This means accessibility improvements like ARIA labels (e.g. `aria-label="Changer de thème"`) need to be applied in batch using a script to maintain consistency.
**Action:** Implemented a batch processing script to add the missing `aria-label` to `#themeBtn` elements across all HTML files, making sure to open files in binary mode to preserve line endings.
