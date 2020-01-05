import time
#import pyfiglet # Did not use
import os
from art import *

##def clear():
##    os.system('cls' if os.name == 'nt' else 'clear')
 

## "%Z"- Adds the Current Time Zone of Time

##-- Clear Screen Function (Refreshes the Clock)
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


while True:

    print("<-----ASCII Digital Clock----->")
    print("Created by EarlierMeat1", '\n')

    ##-- Collects Current Date
    print("The Current Date & Time:")

    date = time.strftime('%A %d %B %Y')
    day = time.strftime('%d')
    mon = time.strftime('%b')
    wDay = time.strftime('%A')

    dm = day + " " + mon
    print(date)

    ##-- Prints Current Date as ASCII
    tprint(wDay,font="block", chr_ignore=True)
    tprint(dm,font="block", chr_ignore=True)    

    ##-- Collects Current Time
    time2 = time.strftime('%H:%M:%S')
    print("\r", time2, end="")
    print()

    ##-- Prints Current Time in ASCII
    set_default(overwrite=True)
    tprint(time2)
    time.sleep(0.1)
    clear()

##    ascii_time = pyfiglet.figlet_format(time2)
##    print("\r", ascii_time)
    
    



