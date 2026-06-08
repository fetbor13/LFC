## 2024-05-18 - [Add aria-label to theme button]
**Learning:** The theme toggle buttons in the app use emoji for visual representation and lack descriptive text, presenting a barrier to screen readers. For icon-only buttons, `aria-label` must be explicitly provided in French to support accessibility.
**Action:** Add `aria-label="Changer de thème"` to buttons toggling themes across the application.
