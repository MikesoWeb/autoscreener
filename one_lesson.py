import os

import pyautogui

full_path = os.path.join(os.getcwd(), "English_phrase")
pyautogui.sleep(1)
for i in range(150):
    img = pyautogui.screenshot(full_path + f"/{i}-english_phrase.jpg")
    pyautogui.sleep(10)
