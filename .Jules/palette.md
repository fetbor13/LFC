
## 2024-05-24 - Missing ARIA Labels on Interactive Elements
**Learning:** Icon-only buttons (like theme toggles and close buttons) and text inputs relying solely on placeholders commonly lack `aria-label` attributes across the application's HTML pages. This degrades screen reader accessibility.
**Action:** When creating or modifying icon-only buttons or placeholder-only inputs, always ensure an appropriate `aria-label` is included (e.g., `aria-label="Fermer"` or `aria-label="Rechercher"`).
