def countdown(x):
    while x > 0:
        print(f"{x} SECOND(S)!")
        x -= 1
    print("HAPPY NEW YEAR!")

import time

def countdown_with_sleep(x):
    while x > 0:
        print(f"{x} SECOND(S)!")
        x -= 1
        time.sleep(1)
    print("HAPPY NEW YEAR!")

