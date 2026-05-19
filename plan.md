1. **Explore `index.html`** to locate icon-only buttons and form inputs that lack ARIA labels.
2. **Apply UX improvements** to `index.html` using targeted merge diffs:
   - Add `aria-label="Changer le thème"` to the theme toggle button.
   - Add `aria-label="Fermer"` to the close buttons (`✕`) in both the Prof and Student modals.
   - Add proper `aria-label` attributes to the password/email text inputs in the modals since they only rely on `placeholder` text (which is bad for screen readers).
   - Add `role="dialog"` and `aria-modal="true"` along with `aria-labelledby` to the modals to improve their accessibility.
3. **Verify** that the page continues to function perfectly and check if `index.html` contains the applied changes.
4. **Log the critical learning** to `.Jules/palette.md`.
5. **Submit** the PR.
