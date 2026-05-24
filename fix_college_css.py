import re
import glob

def fix_css(f):
    with open(f, "r", encoding="utf-8") as file:
        content = file.read()

    # We replaced `Term_chapitre` styles but didn't keep `.sim-screen` or `.flashcard` if they weren't in Term_chapitre
    # Oh wait! The Term_chapitre *does* have .flash-card, .sim-grid, etc.
    # But College uses `.flashcard` and `.flash-inner`.
    # Term uses `.flash-card` and `.flash-inner`.
    # Let's ensure the JS works by patching the HTML classes.
    content = content.replace('class="flashcard"', 'class="flash-card"')

    # For sims, college uses .sim-screen. Let's make sure it's consistent.

    with open(f, "w", encoding="utf-8") as file:
        file.write(content)

for f in glob.glob("*eme_chapitre*.html") + glob.glob("5e_chapitre*.html"):
    fix_css(f)
