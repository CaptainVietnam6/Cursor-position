'''
Copyright (©) 2021 Kiet Pham <kiet.riley2005@gmail.com>

Author Name: Kiet Pham
Author Contact: kiet.riley2005@gmail.com
Discord: CaptainVietnam6#7932
Discord Server: https://discord.gg/3z76p8H5yj
GitHub: https://github.com/CaptainVietnam6
Instagram: @itz_kietttttttttt
Program Status: FINALISED
'''

import pyautogui, sys
print("Press Ctrl-C to quit.")

try:
    while True:
        x, y = pyautogui.position()
        positionStr = "X: " + str(x).rjust(4) + " Y: " + str(y).rjust(4)
        print(positionStr, end='')
        print("\b" * len(positionStr), end = "", flush = True)
except KeyboardInterrupt:
    print("\n")
