from time import sleep
from keyboard import is_pressed
import re
import os
import threading
import graphics
import settings

options = [f"{' '*32}Play", f"{' '*30}Settings", f"{' '*29}Chess Board"]
selections = [f"{' '*32}Play", f"{' '*30}Settings", f"{' '*29}Chess Board"]
selection = 0
canPress = True

def delayButton():
    global canPress
    canPress = False
    sleep(settings.KeyHoldDelay)
    canPress = True

os.system(f'mode con: cols={settings.StartCol} lines={settings.StartLine}') 
WinSize = str(os.get_terminal_size())
os.system('cls')

while True:
    chars = []
    WinSizeNums = [int(num) for num in re.findall(r"\d+", WinSize)]
    print('\033[?25l', end="") # Hides Cursor
    print('\033[999A\033[99999K', end='') # Erases Screen
    chars.append(f"""
                 
    ▄████████    ▄█    █▄       ▄████████    ▄████████    ▄████████ 
    ███    ███   ███    ███     ███    ███   ███    ███   ███    ███ 
    ███    █▀    ███    ███     ███    █▀    ███    █▀    ███    █▀  
    ███         ▄███▄▄▄▄███▄▄  ▄███▄▄▄       ███          ███        
    ███        ▀▀███▀▀▀▀███▀  ▀▀███▀▀▀     ▀███████████ ▀███████████ 
    ███    █▄    ███    ███     ███    █▄           ███          ███ 
    ███    ███   ███    ███     ███    ███    ▄█    ███    ▄█    ███ 
    ████████▀    ███    █▀      ██████████  ▄████████▀   ▄████████▀                                                                
    \n""".center(int(WinSizeNums[0]/2), " "))

    if not options[selection].startswith("\033[92m"):
        options[selection] = "\033[92m" + options[selection] + "\033[0m"

    t = threading.Thread(target=delayButton) # Delay between key presses while holding key down

    # Fix Menu Changing Bug - change terminal controls so they move your selection while being compatiable with any option list thats used   ---- or think of another way to change from start menu
    
    # Terminal Controls
    if is_pressed("down arrow") and canPress:
        if selection + 1 <= (len(options) - 1):
            t.start()
            options[selection] = selections[selection]
            selection += 1
        else:
            t.start()
            options[selection] = selections[selection]
            selection = 0
    elif is_pressed("up arrow") and canPress:
        if selection - 1 >= 0:
            t.start()
            options[selection] = selections[selection]
            selection -= 1
        else:
            t.start()
            options[selection] = selections[selection]
            selection = (len(options) - 1)
    
    for option in options:
        chars.append(option)
        chars.append('\n')
 
    chars.append('\n')
    graphics.Display(chars)

    sleep(0.00000000001)