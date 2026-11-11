## 2024-05-14 - Custom Modal Accessibility
**Learning:** Custom modals in this application lack basic screen reader accessibility without ARIA attributes. Form inputs inside these modals rely entirely on placeholders for labels, which are not reliably announced.
**Action:** When creating or modifying custom modals (e.g. `.modal`), always ensure `role="dialog"`, `aria-modal="true"`, and `aria-labelledby` are used. For form inputs relying on placeholders, strictly ensure they include an appropriate `aria-label`. Ensure icon-only close buttons have `aria-label="Fermer"`.
