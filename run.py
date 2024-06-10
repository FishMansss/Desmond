import pyautogui
x1,y1 = pyautogui.locateCenterOnScreen('newSnap.png', confidence = 0.7)
print(x1,y1)
pyautogui.click(x1,y1)
