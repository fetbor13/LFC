from playwright.sync_api import sync_playwright
import time

def verify():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.set_viewport_size({"width": 1280, "height": 800})

        # Check College 5eme
        page.goto("http://localhost:8000/5eme_chapitre1_ultimate.html")
        time.sleep(1)
        page.screenshot(path="5eme_chap1_ultimate.png")

        # Check PCSI
        page.goto("http://localhost:8000/pcsi_chapitre1_ultimate.html")
        time.sleep(1)
        page.screenshot(path="pcsi_chap1_ultimate.png")

        browser.close()
        print("Screenshots saved: 5eme_chap1_ultimate.png, pcsi_chap1_ultimate.png")

if __name__ == "__main__":
    verify()
