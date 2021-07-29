import pyautogui

pyautogui.keyDown("win")
pyautogui.keyDown("ctrl")

for i in range(0, 1):
    pyautogui.press('d')

while True:
    pyautogui.keyDown("win")
    pyautogui.keyDown("ctrl")
