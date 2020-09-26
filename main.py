import pyautogui
from pyscreeze import ImageNotFoundException
import time

TARGET_SIPS = 100 # Target sips. 100 for the achievement.

START_DELAY = 5 # Delay after program start for you to enter game

#====================================================
# The defaults below should work for 16:9 screens. If they don't and
# the bot cannot locate, then mess with it a bit.
(SCREEN_WIDTH, SCREEN_HEIGHT) = pyautogui.size()
CUP_X = SCREEN_WIDTH * 0.081 # Calculate x-pos of the coffee mug
CUP_Y = SCREEN_HEIGHT * 0.847 # Calculate y-pos of the coffee mug
RESTART_X = SCREEN_WIDTH * 0.497 # Calculate x-pos of the restart button
RESTART_Y = SCREEN_HEIGHT * 0.752 # Calculate y-pos of the restart button

SIPS = 2 # Sometimes there are 3 sips, but usually 2. Probably do not alter.
DRINK_INTERVAL = 4.35 # Interval per sip. Probably do not alter.
RESTART_DELAY = 0.4 # Delay between clicking restarting and beginning sip.


def main():
    print('Tab into the game now. You have', START_DELAY, 'seconds.\n')
    time.sleep(START_DELAY)

    sips = 0
    locations = locate()
    print(locations)

    while sips < TARGET_SIPS:
        pyautogui.click(x=locations["cup"][0], y=locations["cup"][1],
                        clicks=SIPS, interval=DRINK_INTERVAL, button='left')
        sips += SIPS
        pyautogui.press('esc')
        pyautogui.click(x=locations["restart"][0], y=locations["restart"][1],
                        button='left')
        if sips % 10 == 0:
            print('Reached', sips, 'sips.')
        time.sleep(RESTART_DELAY)
    
    print('Target reached. Bot terminated.')
    pyautogui.confirm('Target reached. Bot terminated.')

def locate():
    locations = {
        "cup": (CUP_X, CUP_Y),
        "restart": (RESTART_X, RESTART_Y)
    }

    return locations   
    

if __name__ == "__main__":
    main()