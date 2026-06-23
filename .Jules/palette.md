## 2024-11-20 - Adding ARIA labels to buttons

**Learning:** When navigating standard custom modals or performing standard actions (like changing themes or opening menus) with icon-only or poorly described buttons, accessibility suffers greatly for screen readers. Buttons like `✕` or `🌙` or `Prof` lack sufficient context without `aria-label`.
**Action:** Consistently add clear `aria-label` to these interactive elements (e.g. `aria-label="Fermer la modale professeur"` and `aria-label="Changer de thème"`). It makes the interface significantly more accessible for screen reader users and improves the overall semantic value of the HTML.
