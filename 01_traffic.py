from gpiozero import LED
from time import sleep

red_led = LED(17)
yellow_led = LED(22)
green_led = LED(27)

while True:
    red_led.on()
    sleep(1)
    yellow_led.on()
    sleep(1)
    red_led.off()
    sleep(1)
    yellow_led.off()
    green_led.on()
    sleep(2.5)
    green_led.off()