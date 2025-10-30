import mouse
import keyboard
import time

isClicking = False
t = 10
print(f'Программа запущена\nВыбранный интервал времени {t}\nЧтобы начать нажмите Alt + Z')

def set_clicker():
    global isClicking
    if isClicking:
        isClicking = False
        print('Кликер отключен')
    else:
        isClicking = True
        print('Кликер включен')

keyboard.add_hotkey('Alt + Z', set_clicker)

while True:
    if isClicking:
        mouse.double_click(button='left')
        time.sleep(t)

