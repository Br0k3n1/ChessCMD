from time import sleep
from keyboard import is_pressed
import threading
import graphics

options = ["Play", "Settings", "Chess Board"]
selections = ["Play", "Settings", "Chess Board"]
selection = 0
while True:
    chars = []
    print('\033[99A\033[99999K', end='')
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

    # Fix by having a thread force a delay by using sleep function
    if is_pressed("down arrow"):
        if selection + 1 <= (len(options) - 1):
            options[selection] = selections[selection]
            selection += 1
        else:
            options[selection] = selections[selection]
            selection = 0
    elif is_pressed("up arrow"):
        if selection - 1 >= 0:
            options[selection] = selections[selection]
            selection -= 1
        else:
            options[selection] = selections[selection]
            selection = (len(options) - 1)
    
    for option in options:
        chars.append(option)
    chars.append(str(selection))
    
    graphics.Display(chars)

    sleep(0.00000000001)

