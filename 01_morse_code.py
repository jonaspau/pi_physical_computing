# A small file to blink morse code on a led accepting any input
# LED should be connected to pin 17

from gpiozero import LED
from time import sleep

morse_lib = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',     'F': '..-.',
    'G': '--.',   'H': '....',  'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',   'P': '.--.',  'Q': '--.-',  'R': '.-.',
    'S': '...',   'T': '-',     'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-','-': '-....-','/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.','=': '-...-', '+': '.-.-.', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-','!': '-.-.--','?': '..--..','@': '.--.-.'
}

# LED GPIO
led = LED(17)

# Timing
dot_time = 0.2
dash_time = dot_time * 3
letter_end = dot_time * 3
word_end = dot_time * 7


def main():
    message = get_message()
    blink_message(message)

# Iterate through each letter, and match it with the morse_lib dictionary:
def blink_message(msg):
    for letter in msg:
        if letter == " ":
            sleep(word_end)
        else:
            for symbol in morse_lib.get(letter.upper(), ""):
                if symbol == ".":
                    led.on()
                    sleep(dot_time)
                elif symbol == "-":
                    led.on()
                    sleep(dash_time)
                led.off()
                sleep(dot_time)
            sleep(letter_end - dot_time)


def get_message():
    message = input("Enter messsage to encode to morse: ")
    return message


if __name__ == "__main__":
    main()