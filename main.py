from time import sleep
from keyboard import is_pressed
import os
import threading
import graphics

options = ["Play", "Settings", "Chess Board"]
selections = ["Play", "Settings", "Chess Board"]
selection = 0
canPress = True

def delayButton():
    global canPress
    canPress = False
    sleep(0.1)
    canPress = True

os.system('cls')
while True:
    chars = []
    print('\033[?25l', end="") # Hides Cursor
    print('\033[999A\033[99999K', end='') # Erases Screen
    chars.append("""

    ▄████████    ▄█    █▄       ▄████████    ▄████████    ▄████████ 
    ███    ███   ███    ███     ███    ███   ███    ███   ███    ███ 
    ███    █▀    ███    ███     ███    █▀    ███    █▀    ███    █▀  
    ███         ▄███▄▄▄▄███▄▄  ▄███▄▄▄       ███          ███        
    ███        ▀▀███▀▀▀▀███▀  ▀▀███▀▀▀     ▀███████████ ▀███████████ 
    ███    █▄    ███    ███     ███    █▄           ███          ███ 
    ███    ███   ███    ███     ███    ███    ▄█    ███    ▄█    ███ 
    ████████▀    ███    █▀      ██████████  ▄████████▀   ▄████████▀  
                                                                    
    \n""")

    if not options[selection].startswith("\033[92m"):
        options[selection] = "\033[92m" + options[selection] + "\033[0m"

    t = threading.Thread(target=delayButton)

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

    graphics.Display(chars)

    sleep(0.00000000001)
