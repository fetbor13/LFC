import re
import glob

# Load term styles
with open("Term_chapitre1.html", "r", encoding="utf-8") as f:
    term_html = f.read()

term_styles = re.findall(r'(<style.*?>.*?</style>)', term_html, flags=re.DOTALL)
with open("azur_theme.css", "r", encoding="utf-8") as f:
    azur_css = f.read()

# Replace the first style with our azur css
term_styles[0] = azur_css
term_styles_combined = "\n".join(term_styles)

def clean_college_html(f):
    with open(f, "r", encoding="utf-8") as file:
        content = file.read()

    # Extract original font-family
    font_family_match = re.search(r'body\s*\{\s*font-family:\s*([^;}]+)', content)
    font_family = font_family_match.group(1) if font_family_match else ""

    # 1. Remove all old styles
    content = re.sub(r'<style.*?>.*?</style>', '', content, flags=re.DOTALL)

    # 2. Add combined Term+Azur styles
    styles_to_inject = term_styles_combined
    if font_family:
        styles_to_inject += f"\n<style>\nbody {{ font-family: {font_family.strip()}; }}\n</style>"

    content = content.replace('</head>', styles_to_inject + '\n</head>')

    # 3. Structure changes
    content = content.replace('class="sidebar"', 'class="rail"')
    content = content.replace('class="side"', 'class="rail"')
    content = content.replace('class="layout-course"', 'class="course-grid"')
    content = content.replace('class="course"', 'class="course-body"')
    content = content.replace('class="btn primary"', 'class="primary"')
    content = content.replace('class="btn"', 'class="secondary"')
    content = content.replace('class="hero-img"', 'class="real-hero-img"')
    content = content.replace('class="choice"', 'class="option"')

    # Fix branding
    def brand_replace(match):
        h1 = match.group(1)
        p = match.group(2)
        return f'<div class="brand"><div aria-hidden="true" class="brand-mark">PC</div><div><h1>{h1}</h1><p>{p}</p></div></div>'

    content = re.sub(r'<div class="brand">.*?<h1>(.*?)</h1>.*?<p>(.*?)</p>.*?</div>', brand_replace, content, flags=re.DOTALL)

    # Tabs
    def tab_replace(match):
        cls = match.group(1)
        data = match.group(2)
        inner = match.group(3).strip()

        if " " in inner and len(inner.split(" ")[0]) <= 2:
            parts = inner.split(" ", 1)
            icon = parts[0]
            text = parts[1]
        elif len(inner) > 0 and not inner[0].isalnum():
            icon = inner[0:2].strip() if len(inner) > 1 and not inner[1].isalnum() else inner[0]
            text = inner[len(icon):].strip()
        else:
            icon = "📄"
            text = inner

        return f'<button class="tab{cls}" data-tab="{data}" role="tab"><span class="tab-icon">{icon}</span><span class="tab-text">{text}</span></button>'

    content = re.sub(r'<button class="tab(.*?)" data-tab="([^"]+)">(.*?)</button>', tab_replace, content)

    # Wrap tabs in nav if needed
    def wrap_tabs(match):
        tabs = match.group(0)
        if '<nav aria-label=' not in tabs:
            return f'<nav aria-label="Onglets du chapitre" class="tablist" role="tablist">\n{tabs}</nav>\n'
        return tabs

    content = re.sub(r'(<button class="tab[^>]+>.*?</button>\s*)+', wrap_tabs, content)

    # App wrap
    if '<div class="app">' not in content:
        content = content.replace('<body>', '<body>\n<div class="app">')
        content = content.replace('</body>', '</div>\n</body>')

    # Page wrap
    if '<div class="page">' not in content:
        content = re.sub(r'(</nav>|</div>|</header>)\s*<header class="hero">', r'\1\n<div class="page">\n    <header class="hero">', content, count=1)
        content = re.sub(r'(</nav>|</div>|</header>)\s*<div class="hero">', r'\1\n<div class="page">\n    <div class="hero">', content, count=1)
        content = re.sub(r'(</nav>|</div>|</header>)\s*<section class="hero">', r'\1\n<div class="page">\n    <section class="hero">', content, count=1)
        content = re.sub(r'(</div>)\s*<div class="hero">', r'\1\n<div class="page">\n    <div class="hero">', content, count=1)
        content = content.replace('</main>', '</div>\n  </main>')

    # 4eme special tags -> pills?
    content = content.replace('class="tag"', 'class="pill"')

    # Save
    with open(f, "w", encoding="utf-8") as file:
        file.write(content)

    print(f"Processed {f}")

for f in glob.glob("*eme_chapitre*.html") + glob.glob("5e_chapitre*.html"):
    clean_college_html(f)
