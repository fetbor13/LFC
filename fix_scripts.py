import re
import glob

# The 2026-specific JS (canvas starfield)
js_script_2026 = """
// 2026 Ultimate Aesthetics (Canvas)
const canvas=document.getElementById('starfield');
if (canvas) {
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

// Ensure tab switching visually updates the 2026 sidebar tabs correctly
// We hook into the existing switchTab function by overriding it or supplementing it.
const originalSwitchTab = window.switchTab;
if (typeof originalSwitchTab === 'function') {
    window.switchTab = function(tabId) {
        // Call the original logic to handle the panels and history
        originalSwitchTab(tabId);

        // Update the visual state of the 2026 sidebar
        document.querySelectorAll('.tablist .tab').forEach(t => t.classList.remove('active'));
        const targetTab = document.querySelector(`.tablist .tab[data-tab="${tabId}"]`);
        if(targetTab) targetTab.classList.add('active');
    };
}

document.querySelectorAll('.tablist .tab').forEach(btn => {
  btn.addEventListener('click', () => {
    if (typeof window.switchTab === 'function') {
        window.switchTab(btn.dataset.tab);
    }
  });
});
"""

files_to_process = [f for f in glob.glob("*.html") if re.match(r'^(Term|1ere|2nde|3eme|4eme|5eme|5e|pcsi)_.*\.html$', f) and "ultimate" not in f]

for filename in files_to_process:
    print(f"Injecting original JS into {filename.replace('.html', '_ultimate.html')}...")
    with open(filename, 'r', encoding='utf-8') as f:
        original_html = f.read()

    # Extract all the logic script block right before the body close
    match = re.search(r'</main>.*?<script>(.*?)</script>\s*</body>', original_html, re.DOTALL | re.IGNORECASE)
    original_js = match.group(1) if match else ""

    # If not found using that exact pattern, try finding the last script tag
    if not original_js:
        scripts = re.findall(r'<script>(.*?)</script>', original_html, re.DOTALL)
        for s in reversed(scripts):
            if "function " in s or "const " in s or "let " in s:
                original_js = s
                break

    out_name = filename.replace('.html', '_ultimate.html')

    try:
        with open(out_name, 'r', encoding='utf-8') as f:
            ultimate_html = f.read()
    except FileNotFoundError:
        continue

    # Find the current 2026 script block in ultimate_html
    # It starts with <script> and ends with </script>\n</body>
    match_ultimate = re.search(r'<script>\s*const canvas=document\.getElementById.*?switchTab\(btn\.dataset\.tab\);\s*}\);\s*}\);\s*</script>', ultimate_html, re.DOTALL)
    if match_ultimate:
        ultimate_html = ultimate_html.replace(match_ultimate.group(0), "")
    else:
        # try a broader replacement to strip the generated 2026 script
        ultimate_html = re.sub(r'<script>\s*const canvas=document\.getElementById.*?</script>', '', ultimate_html, flags=re.DOTALL)

    # Re-insert the combined script
    combined_script = f"""
<script>
{original_js}
{js_script_2026}
</script>
</body>
"""
    ultimate_html = ultimate_html.replace('</body>', combined_script)

    with open(out_name, 'w', encoding='utf-8') as f:
        f.write(ultimate_html)

print("Done restoring scripts.")
