from gpiozero import Button, LED


btn = Button(4)
led = LED(17)

led_on = False

def toggle_led():
    global led_on
    if led_on:
        led.off()
        print("LED Off")
        led_on = False

    else:
        led.on()
        print("LED on")
        led_on = True

def main():
    print("Wainting for button press")
    btn.when_pressed = toggle_led
        
    while True:
        pass
    

main()