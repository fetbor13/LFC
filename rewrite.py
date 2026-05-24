import glob
import os
import re

css_to_inject = """
<style>
/* ============================================================
   BASE & THEME VARIABLES (AZUR INTENSE & SUPPLEMENTARY COLORS)
   ============================================================ */
:root {
  --bg: #f0f8ff;
  --bg2: #e0f0fe;
  --panel: #ffffff;
  --panel2: #f4faff;
  --line: #bae0ff;
  --line2: #91caff;

  --text: #002244;
  --muted: #004488;
  --faint: #6699cc;

  --blue: #007bff;
  --blue2: #0056b3;
  --blue3: #e6f2ff;

  --green: #28a745;
  --green2: #eaf6ec;

  --amber: #ffc107;
  --amber2: #fff8e1;

  --red: #dc3545;
  --red2: #fdf2f2;

  --mauve: #6f42c1;
  --mauve2: #f4eefe;

  --cyan: #17a2b8;
  --cyan2: #e3f8fb;

  --shadow: 0 18px 38px rgba(0, 34, 68, 0.08);
  --shadow2: 0 10px 24px rgba(0, 34, 68, 0.065);

  --r: 8px;
  --r2: 8px;
  --side: 286px;
  --content: 1280px;
}

[data-theme="dark"] {
  --bg: #001122;
  --bg2: #001a33;
  --panel: #002244;
  --panel2: #003366;
  --line: #004488;
  --line2: #0055aa;

  --text: #e6f2ff;
  --muted: #99ccff;
  --faint: #6699cc;

  --blue: #3399ff;
  --blue2: #66b2ff;
  --blue3: rgba(51, 153, 255, 0.12);

  --green: #4ade80;
  --green2: rgba(74, 222, 128, 0.12);

  --amber: #fbbf24;
  --amber2: rgba(251, 191, 36, 0.12);

  --red: #f87171;
  --red2: rgba(248, 113, 113, 0.12);

  --mauve: #a78bfa;
  --mauve2: rgba(167, 139, 250, 0.16);

  --cyan: #38bdf8;
  --cyan2: rgba(56, 189, 248, 0.13);

  --shadow: 0 18px 44px rgba(0, 0, 0, 0.4);
  --shadow2: 0 10px 30px rgba(0, 0, 0, 0.3);
}

/* Base styles */
body { background: linear-gradient(180deg, var(--bg), var(--bg2)); line-height: 1.62; font-family: 'Inter', sans-serif; color: var(--text); margin: 0; }
a { color: inherit; text-decoration: none; }
* { box-sizing: border-box; }

/* Grid Layout */
.app { display: grid; grid-template-columns: var(--side) minmax(0, 1fr); min-height: 100vh; }
.rail { background: rgba(255, 255, 255, 0.78); backdrop-filter: blur(18px); padding: 18px; border-right: 1px solid var(--line); position: sticky; top: 0; height: 100vh; overflow-y: auto; }
[data-theme="dark"] .rail { background: rgba(0, 34, 68, 0.78); }

/* Sidebar Branding */
.brand { display: flex; align-items: center; gap: 10px; margin-bottom: 18px; }
.brand-mark { width: 44px; height: 44px; border-radius: 8px; background: linear-gradient(135deg, var(--blue), var(--blue2)); box-shadow: var(--shadow); color: white; display: grid; place-items: center; font-weight: bold; }
.brand h1 { font-size: 17px; font-weight: 800; margin: 0; }
.brand p { font-size: 12px; margin: 0; color: var(--muted); }

/* Navigation */
.nav-label { font-size: 11px; margin: 18px 0 8px; font-weight: bold; text-transform: uppercase; color: var(--faint); }
.tablist { display: flex; flex-direction: column; gap: 7px; }
.tab { width: 100%; display: grid; grid-template-columns: 30px 1fr; align-items: center; gap: 9px; border-radius: 8px; padding: 10px; border: 1px solid transparent; font-size: 13px; font-weight: 780; color: var(--muted); cursor: pointer; background: transparent; text-align: left; }
.tab-icon { width: 28px; height: 28px; border-radius: 8px; display: grid; place-items: center; background: var(--panel); border: 1px solid var(--line); font-size: 14px; line-height: 1; }
.tab-text { min-width: 0; }
.tab:hover { border-color: var(--line); background: var(--panel); color: var(--text); }
.tab.active { border-color: rgba(0, 123, 255, 0.35); background: var(--blue3); color: var(--blue); box-shadow: inset 4px 0 0 var(--blue); }

/* Main Content Area */
.main { min-width: 0; display: flex; flex-direction: column; }
.topbar { height: 58px; background: rgba(246, 248, 251, 0.84); padding: 0 24px; display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid var(--line); position: sticky; top: 0; z-index: 10; backdrop-filter: blur(10px); }
[data-theme="dark"] .topbar { background: rgba(11, 16, 24, 0.84); }
.crumb { font-size: 13px; color: var(--muted); }
.crumb b { color: var(--blue); }
.page { max-width: 1280px; padding: 22px; width: 100%; margin: 0 auto; }

/* Hero Section */
.hero { display: grid; grid-template-columns: minmax(0, 1.04fr) minmax(340px, 0.96fr); gap: 16px; margin-bottom: 16px; }
.hero-card { border-radius: 8px; padding: 22px; box-shadow: var(--shadow); min-height: 214px; background: var(--panel); position: relative; overflow: hidden; }
.hero-card:before { content: ""; position: absolute; inset: 0; background: radial-gradient(circle at top right, rgba(0, 123, 255, 0.09), transparent 68%); pointer-events: none; }
.eyebrow { color: var(--blue); font-weight: 800; font-size: 12px; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 8px; }
.instructor { color: var(--muted); font-size: 12px; display: flex; align-items: center; gap: 6px; }
.instructor:before { content: ""; width: 6px; height: 6px; border-radius: 50%; background: var(--blue); }
.hero h2 { font-size: clamp(31px, 4.2vw, 42px); line-height: 1.02; font-weight: 800; letter-spacing: -0.045em; margin: 10px 0 12px; }
.hero h2 span { color: var(--blue); }
.hero-copy { color: var(--muted); font-size: 15px; max-width: 72ch; margin-bottom: 0; }
.hero-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; margin-top: 16px; }
.metric { border-radius: 8px; background: var(--bg); padding: 10px; border: 1px solid var(--line); }
.metric b { display: block; font-size: 20px; color: var(--text); line-height: 1; }
.metric span { display: block; font-size: 12px; color: var(--muted); margin-top: 4px; }
.real-hero-img { height: clamp(150px, 16vw, 200px) !important; min-height: 0 !important; max-height: 200px !important; align-self: start; background: var(--panel2); border-radius: 8px; overflow: hidden; border: 1px solid var(--line); margin: 0; }
.real-hero-img img { width: 100%; height: 100%; object-fit: cover; object-position: center; display: block; }

/* Panels & Content */
.panel { display: none; scroll-margin-top: 78px; }
.panel.active { display: block; }
.content-card, .card, .sim-card, .ai-card, .quiz-card, details.exercise, .fc-card, .mindmap, .formula, .table-wrap, .box, .example-box, .fig, .sim-select, .titrage-grid input, .result, .canvas-box { border-radius: 8px; }
.content-card { box-shadow: var(--shadow); padding: 20px; background: var(--panel); border: 1px solid var(--line); margin-bottom: 16px; }
.content-card h3 { font-size: 25px; font-weight: 800; margin-top: 0; margin-bottom: 16px; }
.course-grid { display: grid; grid-template-columns: 158px minmax(0, 1fr); gap: 24px; }

/* Table of Contents */
.toc { position: sticky; top: 78px; }
.toc-title { font-size: 10px; font-weight: 800; letter-spacing: 0.15em; text-transform: uppercase; color: var(--faint); margin-bottom: 10px; }
.toc a { display: flex; align-items: center; gap: 8px; margin-bottom: 8px; border: 1px solid var(--line); border-left-width: 1px; border-radius: 8px; background: var(--panel); padding: 8px 9px; font-weight: 760; font-size: 12px; transition: 0.2s; }
.toc a:nth-of-type(1) { background: var(--blue3); color: var(--blue); }
.toc a:nth-of-type(2) { background: var(--amber2); color: var(--amber); }
.toc a:nth-of-type(3) { background: var(--green2); color: var(--green); }
.toc a:nth-of-type(4) { background: var(--mauve2); color: var(--mauve); }
.toc a:nth-of-type(5) { background: var(--cyan2); color: var(--cyan); }
.toc a.active { box-shadow: inset 4px 0 0 currentColor; border-color: currentColor; transform: translateX(2px); }

/* Course Body */
.course-body { max-width: 920px; min-width: 0; }
.course-body h2, .section-title { color: var(--blue); font-weight: 800; font-size: 22px; margin: 28px 0 12px; padding-bottom: 8px; border-bottom: 1px solid var(--line); }
.course-body h2:first-child { margin-top: 0; }
.course-body h3 { font-weight: 800; font-size: 16px; margin: 20px 0 10px; color: var(--text); }
.course-body p, .course-body li { color: var(--muted); font-size: 15px; }

/* Boxes */
.box { background: var(--panel); border-top: 1px solid var(--line); border-right: 1px solid var(--line); border-bottom: 1px solid var(--line); border-left: 4px solid; border-radius: 0 8px 8px 0; padding: 16px 18px; margin: 18px 0; box-shadow: var(--shadow2); }
.box-label { font-size: 10px; font-weight: 800; letter-spacing: 0.14em; text-transform: uppercase; margin-bottom: 7px; display: block; }
.box.def { border-left-color: var(--blue); }
.box.def .box-label { color: var(--blue); }
.box.method { border-left-color: var(--cyan); }
.box.method .box-label { color: var(--cyan); }
.box.warn { border-left-color: var(--amber); }
.box.warn .box-label { color: var(--amber); }
.box.ok { border-left-color: var(--green); }
.box.ok .box-label { color: var(--green); }
.box strong { color: var(--text); }

/* Formula */
.formula { background: var(--panel2); padding: 14px; margin: 14px 0; text-align: center; border: 1px solid var(--line); overflow-x: auto; font-family: 'IBM Plex Mono', monospace; }

/* Grid / Cards */
.grid, .grid3, .cards { display: grid; gap: 16px; margin: 16px 0; }
.grid, .cards { grid-template-columns: repeat(2, minmax(0, 1fr)); }
.grid3 { grid-template-columns: repeat(3, minmax(0, 1fr)); }
.card { background: var(--panel); border: 1px solid var(--line); padding: 18px; box-shadow: var(--shadow2); }
.card h3, .card h4 { margin: 0 0 8px; font-size: 16px; font-weight: 760; color: var(--text); }
.card p, .card li { color: var(--muted); font-size: 14px; margin: 0; }

/* Tables */
.table-wrap { overflow: auto; border: 1px solid var(--line); border-radius: 8px; background: var(--panel); box-shadow: var(--shadow2); margin: 15px 0; }
table { border-collapse: collapse; width: 100%; min-width: 600px; }
th, td { text-align: left; padding: 11px 13px; border-bottom: 1px solid var(--line); font-size: 14px; color: var(--muted); }
th { background: var(--panel2); color: var(--faint); font-size: 12px; text-transform: uppercase; letter-spacing: 0.05em; font-weight: 800; }

/* Simulations */
.sim, .sim-grid, .sim-grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0; }
.sim-screen, .sim-card { min-height: 260px; border: 1px solid var(--line); border-radius: 8px; background: var(--panel2); padding: 16px; overflow: hidden; box-shadow: var(--shadow2); }
.control { display: grid; gap: 10px; margin-bottom: 10px; }
.field label, .control label { display: block; font-size: 12px; color: var(--faint); font-weight: 800; margin-bottom: 5px; }
input[type=range], select, input[type=number] { width: 100%; padding: 10px; border: 1px solid var(--line2); border-radius: 8px; background: var(--panel); color: var(--text); font-family: inherit; }
.status, .sim-result { margin-top: 10px; background: var(--blue3); border: 1px solid var(--line2); border-radius: 8px; padding: 12px; color: var(--muted); font-size: 13px; }

/* Buttons */
.btn, .primary, .secondary { border-radius: 8px; padding: 10px 14px; cursor: pointer; font-weight: 800; font-size: 13px; display: inline-flex; align-items: center; justify-content: center; gap: 8px; transition: 0.2s; border: 1px solid transparent; }
.primary { background: var(--blue); color: white; }
.primary:hover { background: var(--blue2); }
.btn, .secondary { background: var(--panel); border-color: var(--line); color: var(--text); }
.btn:hover, .secondary:hover { border-color: var(--blue); color: var(--blue); background: var(--blue3); }
.btn-row { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 10px; }

/* Flashcards */
.flashcard-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 14px; margin: 16px 0; }
.flashcard { height: 230px; perspective: 1000px; cursor: pointer; margin: 0; }
.flashcard-inner, .flash-inner { position: relative; width: 100%; height: 100%; transform-style: preserve-3d; transition: transform 0.55s; }
.flashcard.flipped .flashcard-inner, .flashcard.flipped .flash-inner { transform: rotateY(180deg); }
.face, .flash-front, .flash-back { position: absolute; inset: 0; backface-visibility: hidden; border: 1px solid var(--line); border-radius: 8px; background: var(--panel); box-shadow: var(--shadow2); display: grid; place-items: center; text-align: center; padding: 20px; }
.face.back, .flash-back { transform: rotateY(180deg); background: var(--panel2); color: var(--muted); }
.face h3 { font-size: 20px; margin: 0; }

/* Quiz */
.quiz-card, .quiz-box { background: var(--panel); border: 1px solid var(--line); border-radius: 8px; padding: 20px; margin-bottom: 14px; box-shadow: var(--shadow2); }
.choice, .option { display: block; width: 100%; text-align: left; margin-top: 8px; border: 1px solid var(--line2); background: var(--panel2); border-radius: 8px; padding: 12px; cursor: pointer; color: var(--text); font-weight: 600; transition: 0.2s; }
.choice:hover, .option:hover { border-color: var(--blue); background: var(--blue3); }
.choice.good, .option.correct { background: var(--green2); border-color: var(--green); color: var(--green); }
.choice.bad, .option.wrong { background: var(--red2); border-color: var(--red); color: var(--red); }

/* Externals / Prompts */
.external-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 12px; margin: 16px 0; }
.external { display: block; background: var(--panel); border: 1px solid var(--line); border-radius: 8px; padding: 18px; text-align: center; box-shadow: var(--shadow2); transition: 0.2s; font-weight: 700; color: var(--text); }
.external:hover { transform: translateY(-2px); border-color: var(--blue); color: var(--blue); }
.prompt, .prompt-box { white-space: pre-wrap; background: var(--panel2); border: 1px dashed var(--line2); border-radius: 8px; padding: 16px; color: var(--muted); font-size: 13px; font-family: 'IBM Plex Mono', monospace; margin-top: 10px; }

/* Responsive */
@media(max-width: 1080px) {
  .app { display: block; }
  .rail { position: relative; height: auto; border-right: 0; border-bottom: 1px solid var(--line); padding: 16px; }
  .hero, .course-grid, .grid, .grid3, .sim, .sim-grid, .sim-grid-2 { grid-template-columns: 1fr; }
  .toc { display: none; }
  .real-hero-img { height: 180px !important; }
}
@media(max-width: 720px) {
  .page { padding: 16px; }
  .hero h2 { font-size: 28px; }
  .hero-grid { grid-template-columns: 1fr; }
}

/* Utilities */
.badge, .pill, .chip { display: inline-flex; align-items: center; border-radius: 999px; padding: 4px 10px; font-size: 11px; font-weight: 800; border: 1px solid var(--line); background: var(--blue3); color: var(--blue); }
.chip.amber { background: var(--amber2); color: var(--amber); border-color: rgba(255, 193, 7, 0.2); }
.chip.green { background: var(--green2); color: var(--green); border-color: rgba(40, 167, 69, 0.2); }
.chip.mauve { background: var(--mauve2); color: var(--mauve); border-color: rgba(111, 66, 193, 0.2); }
</style>
"""

# HTML structure to apply to sidebars to make them consistent
def rewrite_file(filepath):
    print(f"Rewriting {filepath}")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace the entire <style> block(s) with our new uniform CSS.
    content = re.sub(r'<style>.*?</style>', '', content, flags=re.DOTALL)
    content = re.sub(r'<style id="[^"]+">.*?</style>', '', content, flags=re.DOTALL)

    # Inject our new CSS before </head>
    content = content.replace('</head>', css_to_inject + '\n</head>')

    # 2. Add correct layout classes:
    # Ensure body structure is <div class="app"><aside class="rail">...
    content = content.replace('class="sidebar"', 'class="rail"')
    content = content.replace('class="side"', 'class="rail"')

    # Fix branding
    content = re.sub(r'<div class="brand">.*?<h1>(.*?)</h1>.*?<p>(.*?)</p>.*?</div>',
                     r'<div class="brand"><div aria-hidden="true" class="brand-mark">PC</div><div><h1>\1</h1><p>\2</p></div></div>',
                     content, flags=re.DOTALL)

    # 3. Modify tab structure to match Term_chapitre
    # It seems in some college files, tabs are like: <button class="tab" data-tab="cours">📘 Cours interactif</button>
    def repl_tab(m):
        cls = m.group(1)
        data = m.group(2)
        icon = m.group(3).strip()
        text = m.group(4).strip()
        # Fallback if icon is missing or merged
        if len(icon) > 2 and " " in icon:
            parts = icon.split(" ", 1)
            icon = parts[0]
            text = parts[1] + " " + text
        elif len(icon) > 2:
            text = icon + text
            icon = "📄"

        return f'<button class="tab {cls}" data-tab="{data}" role="tab"><span class="tab-icon">{icon}</span><span class="tab-text">{text}</span></button>'

    # Simple regex to catch the emoji and text
    content = re.sub(r'<button class="tab(.*?)" data-tab="([^"]+)">(.*?)\s+(.*?)</button>', repl_tab, content)

    # 4. Standardize hero image to `.real-hero-img` instead of `.hero-img`
    content = content.replace('class="hero-img"', 'class="real-hero-img"')

    # 5. Fix up section layout classes
    content = content.replace('class="layout-course"', 'class="course-grid"')
    content = content.replace('class="course"', 'class="course-body"')

    # 6. Apply button standard classes
    content = content.replace('class="btn primary"', 'class="primary"')
    content = content.replace('class="btn"', 'class="secondary"')

    # 7. Minor cleanup for options
    content = content.replace('class="choice"', 'class="option"')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for f in glob.glob("*eme_chapitre*.html"):
    rewrite_file(f)
for f in glob.glob("5e_chapitre*.html"):
    rewrite_file(f)
