import os
from time import sleep
from keyboard import is_pressed

options = ["Play", "Settings", "Chess Board"]
while True:
    os.system('cls')
    print("""

    ▄████████    ▄█    █▄       ▄████████    ▄████████    ▄████████ 
    ███    ███   ███    ███     ███    ███   ███    ███   ███    ███ 
    ███    █▀    ███    ███     ███    █▀    ███    █▀    ███    █▀  
    ███         ▄███▄▄▄▄███▄▄  ▄███▄▄▄       ███          ███        
    ███        ▀▀███▀▀▀▀███▀  ▀▀███▀▀▀     ▀███████████ ▀███████████ 
    ███    █▄    ███    ███     ███    █▄           ███          ███ 
    ███    ███   ███    ███     ███    ███    ▄█    ███    ▄█    ███ 
    ████████▀    ███    █▀      ██████████  ▄████████▀   ▄████████▀  
                                                                    
    \n""")

    for option in options:
        print(option)

    if is_pressed("down arrow") or is_pressed("up arrow"):
        for option in options:
            pass

    sleep(0.00000000000000001)

