## 2024-05-14 - [Accessibility Modals]
**Learning:** The application uses custom modals (e.g., student login, professor login) that lack proper ARIA attributes, making them inaccessible to screen readers. Form inputs also rely only on placeholders without visible labels or ARIA labels.
**Action:** Always add `role="dialog"`, `aria-modal="true"`, and `aria-labelledby` to custom modals. Add `aria-label` to form inputs that lack visible `<label>` elements.
