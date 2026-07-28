## 2024-05-18 - Modals and Inputs ARIA labels
**Learning:** Modals and inputs inside them often lack accessible labels by default when relying only on visual placeholders and structural text.
**Action:** Always add `role="dialog"`, `aria-modal="true"`, and `aria-labelledby` to `.modal-overlay` wrappers, and `aria-label` to visually unlabelled `.stu-field` or similar inputs. Add `aria-label="Fermer"` to icon-only `✕` close buttons and `aria-label="Changer de thème"` to theme toggle buttons.
