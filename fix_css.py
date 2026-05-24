import re

with open("azur_theme.css", "r", encoding="utf-8") as f:
    azur_css = f.read()

# Make sure all blue variables in light and dark mode are correctly replaced
light_vars = r"""  --bg:#f0f8ff;--bg2:#e6f2ff;--panel:#ffffff;--panel2:#f4faff;--line:#bae0ff;--line2:#91caff;
  --text:#001a33;--muted:#004080;--faint:#6699cc;
  --blue:#007fff;--blue2:#005ce6;--blue3:#e6f2ff;
  --green:#28a745;--green2:#eaf6ec;--amber:#ffc107;--amber2:#fff8e1;--red:#dc3545;--red2:#fdf2f2;
  --mauve:#6f42c1;--mauve2:#f4eefe;--cyan:#00bfff;--cyan2:#e6f9ff;
"""

dark_vars = r"""  --bg:#001122;--bg2:#001a33;--panel:#002244;--panel2:#003366;--line:#004080;--line2:#005ce6;
  --text:#e6f2ff;--muted:#80bfff;--faint:#4d99e6;
  --blue:#3399ff;--blue2:#66b2ff;--blue3:rgba(51,153,255,.15);
  --green:#4ade80;--green2:rgba(74,222,128,.12);--amber:#fbbf24;--amber2:rgba(251,191,36,.12);
  --red:#f87171;--red2:rgba(248,113,113,.12);--mauve:#a78bfa;--mauve2:rgba(167,139,250,.16);--cyan:#38bdf8;--cyan2:rgba(56,189,248,.13);
"""

# Replace the original :root values
azur_css = re.sub(r':root\s*\{[^}]+\}', f':root{{\n{light_vars}  --shadow:0 18px 38px rgba(0,34,68,.08);--shadow2:0 10px 24px rgba(0,34,68,.065);\n  --r:8px;--r2:8px;--side:286px;--content:1280px;\n}}', azur_css, count=1)

# Replace the original [data-theme="dark"] values
azur_css = re.sub(r'\[data-theme="dark"\]\s*\{[^}]+\}', f'[data-theme="dark"]{{\n{dark_vars}  --shadow:0 18px 44px rgba(0,0,0,.4);--shadow2:0 10px 30px rgba(0,0,0,.3);\n}}', azur_css, count=1)

with open("azur_theme.css", "w") as f:
    f.write(azur_css)

print("Saved updated Azur intense CSS!")
