import glob
import re

files = glob.glob("Term_chapitre*_ultimate.html")

for filename in files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # We want to replace onclick="document.getElementById('chatIn').value="SOMETHING""
    # with onclick="document.getElementById('chatIn').value='SOMETHING'"

    # regex pattern to match: onclick="document.getElementById('chatIn').value=" (.*?) ""
    # We have to be careful about escaped characters or other things.

    def repl(m):
        inner_val = m.group(1)
        # escape single quotes inside inner_val just in case
        inner_val = inner_val.replace("'", "\\'")
        return f'onclick="document.getElementById(\'chatIn\').value=\'{inner_val}\'"'

    new_content = re.sub(r'onclick="document\.getElementById\(\'chatIn\'\)\.value="(.*?)"+', repl, content)

    if new_content != content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed quotes in {filename}")
