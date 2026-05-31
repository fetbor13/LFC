## 2024-05-18 - Missing ARIA Labels on Icon Buttons
**Learning:** Found a widespread pattern across the application where icon-only buttons, specifically the modal close buttons containing only the '✕' character, are missing `aria-label` attributes. This makes them inaccessible to screen reader users who cannot see or interpret the visual icon accurately (often read out as "multiplication x").
**Action:** Always add `aria-label="Fermer"` to icon-only close buttons. I will implement a global search and replace to fix this specific issue on all instances across the codebase.
