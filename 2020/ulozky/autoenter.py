import pyautogui, time
print('w')
pyautogui.typewrite('hello')
time.sleep(5)
while True:
    pyautogui.press('enter')
    time.sleep(0.1)