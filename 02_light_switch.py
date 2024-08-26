from gpiozero import Button, LED
from time import sleep

btn = Button(4)
led = LED(17)

led.off()

while True:
    if btn.is_pressed:
        print("Oh no, button pressed")
        led.on()
        sleep(5)
        led.off()