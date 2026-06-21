
## 2024-05-18 - Missing ARIA Labels on Icon Buttons
**Learning:** Found multiple instances where the theme toggle button (icon-only `🌙`/`☀️`) lacked an `aria-label`, creating a poor experience for screen readers relying only on visual cues. Due to duplicated components across standalone HTML files, missing aria-labels can easily propagate to many files.
**Action:** Always verify icon-only buttons have an appropriate `aria-label` attribute (e.g. `aria-label="Changer de thème"`) when creating or reviewing interactive elements in all HTML files. Added aria-labels to all instances of `id="themeBtn"`.
