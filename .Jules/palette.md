## 2026-05-22 - Added proper ARIA attributes to modal overlays and form inputs
**Learning:** Found custom modal implementations (`.modal-overlay`) missing critical ARIA attributes (`role="dialog"`, `aria-modal="true"`, `aria-labelledby`) and form inputs relying purely on placeholders without labels or `aria-label`. These were present in multiple layout files (`index.html`, `index_college.html`).
**Action:** Always ensure custom modals have the necessary dialog roles and labels, and any inputs without visual labels explicitly use `aria-label` for screen reader accessibility.
