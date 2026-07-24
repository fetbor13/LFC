import bs4
import copy
import subprocess

# 1. First, we need the original HTML. We can get it from git.
subprocess.run(['git', 'show', '343f717:Term_chapitre7.html'], stdout=open('Term_chapitre7_orig.html', 'w'))

with open('Term_chapitre7_orig.html', 'r', encoding='utf-8') as f:
    orig = f.read()

# Fix the specific inline slash fraction requested by the user
orig = orig.replace(r'\(T^2/a^3\)', r'\(\frac{T^2}{a^3}\)')
# A few more standard ones if they exist
orig = orig.replace(r'\(v = \sqrt{G M / r}\)', r'\(v = \sqrt{\frac{G M}{r}}\)')
orig = orig.replace(r'\(v=\sqrt{G M_{T}/(R_{T}+h)}\)', r'\(v=\sqrt{\frac{G M_{T}}{R_{T}+h}}\)')

with open('astrolabe_template.html', 'r', encoding='utf-8') as f:
    astro = f.read()

soup_orig = bs4.BeautifulSoup(orig, 'html.parser')
soup_astro = bs4.BeautifulSoup(astro, 'html.parser')

panels_to_ensure = ['schemas', 'flash', 'quiz', 'sim', 'exos', 'methodes', 'ia', 'sup']
main_container = soup_astro.find('main', class_='content-overlay')

# Create missing astrolabe panels
if main_container:
    for p in panels_to_ensure:
        pid = f"panel-{p}"
        if not main_container.find('article', id=pid):
            new_article = soup_astro.new_tag('article', id=pid, **{'class': 'glass-panel'})
            main_container.append(new_article)

# Check if panel-cours is missing in astrolabe_template
if not soup_astro.find('article', id='panel-cours'):
    c = soup_astro.new_tag('article', id='panel-cours', **{'class': 'glass-panel active'})
    main_container.insert(0, c)

tab_map = {
    'panel-cours': 'panel-cours',
    'panel-mindmap': 'panel-schemas',
    'panel-flashcards': 'panel-flash',
    'panel-quiz': 'panel-quiz',
    'panel-simulations': 'panel-sim',
    'panel-exercices': 'panel-exos',
    'panel-outils': 'panel-methodes',
    'panel-ece': 'panel-sup',
}

for orig_id, astro_id in tab_map.items():
    orig_tab = soup_orig.find('div', id=orig_id)
    astro_tab = soup_astro.find('article', id=astro_id)
    if orig_tab and astro_tab:
        astro_tab.clear()
        for child in orig_tab.children:
            astro_tab.append(copy.copy(child))

orig_prepa = soup_orig.find('div', id='panel-prepa')
astro_vers = soup_astro.find('article', id='panel-sup')
if orig_prepa and astro_vers:
    astro_vers.append(soup_orig.new_tag("hr", **{'class':'mt-5 mb-5'}))
    for child in orig_prepa.children:
        astro_vers.append(copy.copy(child))


scripts_to_add = []
for script in soup_orig.find_all('script'):
    if script.string:
        if 'fcData' in script.string or 'function initFC' in script.string or 'function verifierReponse' in script.string or 'const q' in script.string or 'quiz' in script.string.lower() or 'flashcard' in script.string.lower() or 'calcul' in script.string.lower() or 'function cal' in script.string:
             scripts_to_add.append(script)

body = soup_astro.find('body')
if body:
    for s in scripts_to_add:
        if 'MathJax =' in s.string and 'MathJax =' in astro:
             continue
        body.append(copy.copy(s))

style_str = """
<style>
/* Adapt original content to dark astrolabe theme */
#panel-cours, #panel-schemas, #panel-flash, #panel-quiz, #panel-sim, #panel-exos, #panel-methodes, #panel-sup {
    color: #e0e0e0;
}
.content-card, .box, .box-green, .box-blue, .box-red, .box-grey, .exo-card, .exo-header {
    background: rgba(255, 255, 255, 0.03) !important;
    border: 1px solid rgba(255, 204, 0, 0.1) !important;
    color: #e0e0e0 !important;
}
.box-title {
    color: #ffcc00 !important;
}
h2, h3, h4, h5 {
    color: #ffcc00;
}
.accordion-button {
    background: rgba(255,255,255,0.05) !important;
    color: #e0e0e0 !important;
}
.accordion-body {
    background: rgba(0,0,0,0.3) !important;
    color: #e0e0e0;
}
.flashcard {
    background: rgba(255,255,255,0.05) !important;
    border: 1px solid rgba(255,204,0,0.2) !important;
    color: #e0e0e0 !important;
}
.flashcard-inner {
    background: transparent !important;
}
.flashcard-front, .flashcard-back {
    background: rgba(25, 30, 45, 0.9) !important;
    color: #e0e0e0 !important;
    border: 1px solid rgba(255, 204, 0, 0.2);
}
.quiz-question {
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 204, 0, 0.1);
    padding: 15px;
    border-radius: 8px;
    margin-bottom: 15px;
}
.quiz-options label {
    color: #e0e0e0;
    display: block;
    padding: 8px;
    background: rgba(0,0,0,0.2);
    border-radius: 4px;
    margin-bottom: 5px;
    cursor: pointer;
}
.quiz-options label:hover {
    background: rgba(255,204,0,0.1);
}
table {
    color: #e0e0e0 !important;
}
th {
    background-color: rgba(255, 204, 0, 0.1) !important;
}
svg {
    max-width: 100%;
}

/* Fallback / Graceful degradation for IE */
@media all and (-ms-high-contrast: none), (-ms-high-contrast: active) {
    .glass-panel {
        background-color: #0a0f19 !important;
        border: 1px solid #d4af37 !important;
        display: block !important;
        margin-bottom: 20px;
    }
    #nbody-canvas {
        display: none !important;
    }
    body {
        overflow: auto !important;
        background-color: #05080e !important;
    }
    .content-overlay {
        position: static !important;
        height: auto !important;
        overflow: visible !important;
        display: block !important;
    }
}
</style>
"""
head = soup_astro.find('head')
if head:
    head.append(bs4.BeautifulSoup(style_str, 'html.parser'))


with open('Term_chapitre7.html', 'w', encoding='utf-8') as f:
    f.write(str(soup_astro))
