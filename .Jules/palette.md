## 2024-05-19 - Adding ARIA labels to Icon-only theme buttons

**Learning:** Across this large set of static HTML files, the global `#themeBtn` (moon icon) frequently lacked an `aria-label`. Without proper text alternatives, screen reader users only hear "button" or the moon emoji representation without understanding its function.

**Action:** Standardize the inclusion of `aria-label="Changer de thème"` on all icon-only theme toggle buttons, regardless of academic level. Use batch scripts to update across all static HTML files to ensure consistency.
