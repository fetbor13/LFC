import re
import glob

def process_file(f):
    with open(f, "r", encoding="utf-8") as file:
        content = file.read()

    # Let's fix the `<button class="tab..."` text processing if we lost text
    # In my previous python script:
    # return f'<button class="tab{cls}" data-tab="{data}" role="tab"><span class="tab-icon">{icon}</span><span class="tab-text">{text}</span></button>'

    # Re-read from git if we messed it up
    pass
