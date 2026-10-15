from playwright.sync_api import sync_playwright
import time
import os

os.makedirs('/home/jules/verification/screenshots', exist_ok=True)
os.makedirs('/home/jules/verification/videos', exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context(
        record_video_dir='/home/jules/verification/videos',
        record_video_size={"width": 1280, "height": 720},
        viewport={"width": 1280, "height": 720}
    )
    page = context.new_page()

    print("Navigating to Chapitre 7...")
    page.goto('http://localhost:3000/Term_chapitre7.html')
    page.wait_for_load_state('networkidle')
    time.sleep(2)

    print("Capturing Cours panel (default)")
    page.screenshot(path='/home/jules/verification/screenshots/final_v2_cours.png', full_page=False)

    print("Navigating to Flashcards panel...")
    page.click("text=Flashcards")
    time.sleep(1)
    page.screenshot(path='/home/jules/verification/screenshots/final_v2_flashcards.png', full_page=False)

    print("Navigating to Quiz panel...")
    page.click("text=Quiz")
    time.sleep(1)
    page.screenshot(path='/home/jules/verification/screenshots/final_v2_quiz.png', full_page=False)

    print("Navigating to Exercises panel...")
    page.click("text=Exercices")
    time.sleep(1)
    page.screenshot(path='/home/jules/verification/screenshots/final_v2_exos.png', full_page=False)


    print("Verification completed successfully.")

    context.close()
    browser.close()
