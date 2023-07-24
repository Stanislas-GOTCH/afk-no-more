import pyautogui as pag
from random import randint

print('Move the mouse to any screen corner to exit')

try:
    while True:
        screen_width, screen_height = pag.size()
        mouse_xpos, mouse_ypos = pag.position(randint(0, screen_width), randint(0, screen_height))

        pag.moveTo(mouse_xpos, mouse_ypos, 0.5)
        pag.PAUSE = 3

except Exception as e:
    print(f'Stopping the script... Bye! {e}')
