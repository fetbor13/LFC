## 2024-05-18 - Missing ARIA Labels on Core Forms & Modals
**Learning:** Found several input fields and close buttons in custom modals (Prof and Student auth) relying entirely on placeholders or generic '✕' characters without accessible text labels. Since they are central entry points (login, registration, search), missing labels block screen reader users.
**Action:** Added targeted `aria-label`s to the main `#themeBtn`, modal `.close` buttons, and all auth/search `input` fields that lacked `<label>` tags in `index.html`.
