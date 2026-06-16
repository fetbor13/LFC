import re
import glob

# Read the 2026 index style template
with open('index_cercle_2026.html', 'r', encoding='utf-8') as f:
    index_2026_html = f.read()

style_match = re.search(r'<style>(.*?)</style>', index_2026_html, re.DOTALL)
style_html = style_match.group(0) if style_match else ""

# Extract the standard tabs from Term_chapitre1.html
with open('Term_chapitre1.html', 'r', encoding='utf-8') as f:
    term1 = f.read()
    standard_tabs_match = re.search(r'<nav aria-label="Onglets du chapitre" class="tablist" role="tablist">(.*?)</nav>', term1, re.DOTALL)
    standard_tabs_html = standard_tabs_match.group(1) if standard_tabs_match else ""

chapter_specific_css = """
<style>
.workspace { grid-template-columns: minmax(220px, 1fr) 3.5fr; }
.tablist { display: flex; flex-direction: column; gap: 8px; margin-top: 16px; }
.tab {
  width: 100%; display: grid; grid-template-columns: 32px 1fr; align-items: center; gap: 10px;
  background: rgba(255,255,255,.03); border: 1px solid rgba(255,255,255,.08);
  border-radius: 14px; padding: 12px; color: var(--muted); font-size: 0.85rem; font-weight: 600;
  text-align: left; cursor: pointer; transition: all 0.2s ease;
}
.tab:hover { background: rgba(255,255,255,.08); border-color: rgba(255,255,255,.15); color: var(--ink); transform: translateX(3px); }
.tab.active {
  background: rgba(var(--active-rgb), .1); border-color: rgba(var(--active-rgb), .4); color: var(--active);
  box-shadow: inset 3px 0 0 var(--active);
}
.tab-icon { font-size: 1.1rem; display: grid; place-items: center; }
.page { padding: 24px; }
.main { overflow-y: auto; max-height: calc(100vh - 80px); }

.course-body { color: var(--ink); line-height: 1.6; }
.hero-card { background: rgba(255,255,255,0.05); border: 1px solid var(--line); backdrop-filter: blur(10px); border-radius: 20px; padding: 24px;}
.hero h2 { font-size: 2.5rem; margin-bottom: 0.5rem; }
.hero h2 span { color: var(--active); }
.metric { background: rgba(0,0,0,0.3); border: 1px solid var(--line); padding: 12px 16px; border-radius: 12px; display: flex; flex-direction: column;}
.metric b { font-size: 1.2rem; color: var(--active); }
.metric span { font-size: 0.8rem; color: var(--muted); }
.useful-card { background: rgba(255,255,255,0.03); border: 1px solid var(--line); backdrop-filter: blur(10px); border-radius: 12px; padding: 16px;}
.content-card { background: rgba(255,255,255,0.03); border: 1px solid var(--line); border-radius: 20px; padding: 24px; backdrop-filter: blur(10px); }
.toc { position: sticky; top: 20px; }
.toc a { display: block; padding: 8px 12px; color: var(--muted); text-decoration: none; border-radius: 8px; font-size: 0.9rem; }
.toc a:hover { background: rgba(255,255,255,0.05); color: var(--ink); }
.course-grid { display: grid; grid-template-columns: 200px 1fr; gap: 32px; }
.hero-grid { display: flex; gap: 16px; margin-top: 16px; flex-wrap: wrap;}
.real-hero-img img { width: 100%; height: 100%; object-fit: cover; border-radius: 12px; }
.useful-strip { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin-top: 24px; margin-bottom: 32px; }
.course-body h3 { color: var(--active); margin-top: 32px; border-bottom: 1px solid var(--line); padding-bottom: 8px; }
.formula { background: rgba(0,0,0,0.4); padding: 16px; border-radius: 12px; border-left: 3px solid var(--active); margin: 16px 0; overflow-x: auto; }
.topbar { background: transparent; padding: 0; height: auto; margin-bottom: 24px; border: none; display: flex; justify-content: space-between; align-items: center; }
.crumb { color: var(--muted); font-size: 0.9rem; }
.crumb b { color: var(--ink); }
.pill-btn { background: rgba(var(--active-rgb), 0.1); border: 1px solid var(--active); color: var(--active); cursor: pointer; transition: 0.2s; border-radius: 999px; font-size: 12px; font-weight: 800; padding: 8px 12px;}
.pill-btn:hover { background: var(--active); color: var(--bg1); }
.box { background: rgba(255,255,255,0.03); border: 1px solid var(--line); border-radius: 12px; padding: 16px; margin: 16px 0;}
.box-green { border-left: 4px solid #a3ff5f; }
.box-yellow { border-left: 4px solid #ffb86b; }
.box-blue { border-left: 4px solid var(--active); }
table { width: 100%; border-collapse: collapse; margin: 16px 0; }
th, td { border: 1px solid var(--line); padding: 8px 12px; text-align: left; }
th { background: rgba(255,255,255,0.05); color: var(--active); }
</style>
"""

js_script_2026 = """
// 2026 Ultimate Aesthetics (Canvas)
const canvas=document.getElementById('starfield');
if(canvas){
    const ctx=canvas.getContext('2d');
    let w=canvas.width=window.innerWidth;
    let h=canvas.height=window.innerHeight;
    const stars=Array.from({length:250},()=>({x:Math.random()*w,y:Math.random()*h,s:Math.random()*1.5,a:Math.random()}));
    function draw(){
      ctx.clearRect(0,0,w,h);
      stars.forEach(st=>{
        st.a+=0.02;
        ctx.fillStyle=`rgba(255,255,255,${Math.abs(Math.sin(st.a))*0.5+0.1})`;
        ctx.beginPath(); ctx.arc(st.x,st.y,st.s,0,Math.PI*2); ctx.fill();
        st.y-=0.2; if(st.y<0) st.y=h;
      });
      requestAnimationFrame(draw);
    }
    draw();
    window.addEventListener('resize',()=>{w=canvas.width=window.innerWidth;h=canvas.height=window.innerHeight;});
}

// Ensure tab switching updates the 2026 sidebar
const originalSwitchTab = window.switchTab;
if (typeof originalSwitchTab === 'function') {
    window.switchTab = function(tabId) {
        originalSwitchTab(tabId);
        document.querySelectorAll('.tablist .tab').forEach(t => t.classList.remove('active'));
        const targetTab = document.querySelector(`.tablist .tab[data-tab="${tabId}"]`);
        if(targetTab) targetTab.classList.add('active');
    };
} else {
    window.switchTab = function(tabId) {
        document.querySelectorAll('.tablist .tab').forEach(t => t.classList.remove('active'));
        const targetTab = document.querySelector(`.tablist .tab[data-tab="${tabId}"]`);
        if(targetTab) targetTab.classList.add('active');

        document.querySelectorAll('.panel').forEach(p => p.classList.remove('active'));
        const targetPanel = document.getElementById('tab-' + tabId);
        if(targetPanel) targetPanel.classList.add('active');
    }
}

document.querySelectorAll('.tablist .tab').forEach(btn => {
  btn.addEventListener('click', () => {
    if (typeof window.switchTab === 'function') {
        window.switchTab(btn.dataset.tab);
    }
  });
});
"""

def clean_colors(html_content):
    html_content = html_content.replace('var(--blue3)', 'rgba(0, 234, 255, 0.1)')
    html_content = html_content.replace('var(--blue)', 'var(--active)')
    html_content = html_content.replace('var(--panel)', 'rgba(255,255,255,0.05)')
    html_content = html_content.replace('var(--amber2)', 'rgba(255, 184, 107, 0.1)')
    html_content = html_content.replace('var(--amber)', '#ffb86b')
    html_content = html_content.replace('var(--mauve2)', 'rgba(255, 107, 214, 0.1)')
    html_content = html_content.replace('var(--mauve)', '#ff6bd6')
    html_content = html_content.replace('var(--green2)', 'rgba(163, 255, 95, 0.1)')
    html_content = html_content.replace('var(--green)', '#a3ff5f')
    html_content = html_content.replace('var(--cyan2)', 'rgba(0, 255, 179, 0.1)')
    html_content = html_content.replace('var(--cyan)', '#00ffb3')
    html_content = html_content.replace('var(--text)', 'var(--ink)')

    # Escape quotes in chatbot suggestions to avoid broken html
    def repl(m):
        inner_val = m.group(1).replace("'", "\\'")
        return f'onclick="document.getElementById(\'chatIn\').value=\'{inner_val}\'"'
    html_content = re.sub(r'onclick="document\.getElementById\(\'chatIn\'\)\.value="(.*?)"+', repl, html_content)
    return html_content

files_to_process = [f for f in glob.glob("*.html") if re.match(r'^(Term|1ere|2nde|3eme|4eme|5eme|5e|pcsi)_.*\.html$', f) and "ultimate" not in f]

for filename in files_to_process:
    print(f"Processing {filename}...")
    with open(filename, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Extract Title
    title_match = re.search(r'<title>(.*?)</title>', html_content)
    title = title_match.group(1) if title_match else "Chapitre (Ultimate)"

    # Extract Main Content
    main_match = re.search(r'<main[^>]*>(.*?)</main>', html_content, re.DOTALL)
    main_html = main_match.group(1) if main_match else ""
    main_html = clean_colors(main_html)

    # Extract Original Javascript
    original_js = ""
    scripts = re.findall(r'<script>(.*?)</script>', html_content, re.DOTALL)
    # The interactive logic is usually in the last or second to last block and contains functions
    for s in reversed(scripts):
        if "function " in s or "const " in s or "let " in s:
            if "MathJax" not in s:
                original_js = s
                break

    # Determine level for header
    level_str = filename.split('_')[0].upper()
    if level_str == "1ERE": level_str = "Première"
    elif level_str == "2NDE": level_str = "Seconde"
    elif level_str == "5E": level_str = "5EME"

    new_html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{title} (2026 Ultimate Edition)</title>
<script>
MathJax = {{
  tex: {{ inlineMath: [['$', '$'], ['\\\\(', '\\\\)']] }},
  options: {{ skipHtmlTags: ['script', 'noscript', 'style', 'textarea'] }}
}};
</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js" async></script>
{style_html}
{chapter_specific_css}
</head>
<body>
<canvas id="starfield"></canvas>
<div class="shell" id="app">
  <header class="topbar" style="border-bottom: 1px solid var(--line); padding-bottom: 16px; margin-bottom: 16px;">
    <div class="brand"><div class="brand-mark">EA</div><div><small>Lycée Français du Caire · M. Borsali</small><strong>{level_str} · Chapitre</strong></div></div>
    <div class="top-actions">
      <button class="ghost-btn" type="button" onclick="window.location.href='index_cercle_2026.html'">Retour à l'accueil</button>
    </div>
  </header>
  <div class="workspace">
    <aside class="side">
      <div class="side-title"><small>Navigation du chapitre</small><strong>Sommaire</strong></div>
      <nav aria-label="Onglets du chapitre" class="tablist" role="tablist">
        {standard_tabs_html}
      </nav>
    </aside>
    <main class="main panel" id="main">
        {main_html}
    </main>
  </div>
</div>
<script>
{original_js}
{js_script_2026}
</script>
</body>
</html>
"""

    out_name = filename.replace('.html', '_ultimate.html')
    with open(out_name, 'w', encoding='utf-8') as f:
        f.write(new_html)

print("All remaining levels processed, including logic scripts.")
