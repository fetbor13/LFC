from playwright.sync_api import sync_playwright
import time

def verify():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.set_viewport_size({"width": 1280, "height": 800})

        # Test Flashcards on Chapter 1
        page.goto("http://localhost:8000/Term_chapitre1_ultimate.html")
        time.sleep(1)

        page.evaluate("if(typeof window.switchTab === 'function') window.switchTab('flashcards')")
        time.sleep(1)

        page.screenshot(path="term1_flashcards_3d.png")
        print("Took screenshot of flashcards tab")

        # Click the first flashcard to test the flip
        cards = page.locator('.fc-card')
        if cards.count() > 0:
            cards.first.click()
            time.sleep(1)
            page.screenshot(path="term1_flashcards_flipped.png")
            print("Took screenshot of flipped flashcard")
        else:
            print("No flashcards found")

        # Test Chatbot on Chapter 10
        page.goto("http://localhost:8000/Term_chapitre10_ultimate.html")
        time.sleep(1)
        page.evaluate("if(typeof window.switchTab === 'function') window.switchTab('quiz')")
        time.sleep(1)
        page.screenshot(path="term10_chatbot.png")
        print("Took screenshot of Chatbot")

        browser.close()

if __name__ == "__main__":
    verify()
