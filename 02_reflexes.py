from gpiozero import Button, LED
from time import time, sleep
from random import randint

led = LED(17)
btn = Button(4)
best_time = 100

while True:
    sleep(randint(1, 10))
    led.on()
    start = time()
    
    btn.wait_for_press()
    led.off()
    end = time()

    reaction_time = round(end - start, 3)
    
    if reaction_time < best_time:
        best_time = reaction_time
        print(f"New record:{reaction_time}!")
    else:
        print(f"Time: {reaction_time}")

