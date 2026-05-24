import re
import glob

def fix_css(f):
    with open(f, "r", encoding="utf-8") as file:
        content = file.read()

    # We replaced `class="sidebar"` with `class="rail"`, but wait: The college files might have CSS specific to "rail" since they had sidebar before.
    # We replaced the `<style>` with Term_chapitre CSS, which contains `.rail` styles! So this is good.

    with open(f, "w", encoding="utf-8") as file:
        file.write(content)

for f in glob.glob("*eme_chapitre*.html") + glob.glob("5e_chapitre*.html"):
    fix_css(f)
