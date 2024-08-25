from gpiozero import LED
from time import sleep

red_led = LED(17)

red_led.toggle()