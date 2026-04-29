import machine
import utime

# Configuración de pines para 12 LEDs
led_pins = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 28, 27]
leds = [machine.Pin(pin, machine.Pin.OUT) for pin in led_pins]

for led in leds:
    led.value(0)

# Configuración de pines para el Teclado Matricial 4x4
row_pins = [26, 22, 21, 20]
col_pins = [19, 18, 17, 16]

rows = [machine.Pin(pin, machine.Pin.OUT) for pin in row_pins]
cols = [machine.Pin(pin, machine.Pin.IN, machine.Pin.PULL_DOWN) for pin in col_pins]

keys = [
    ['1', '2', '3', 'A'],
    ['4', '5', '6', 'B'],
    ['7', '8', '9', 'C'],
    ['*', '0', '#', 'D']
]


def read_keypad():
    for i, row in enumerate(rows):
        row.value(1)
        for j, col in enumerate(cols):
            if col.value() == 1:
                row.value(0)
                return keys[i][j]
        row.value(0)
    return None


while True:
    key = read_keypad()
    if key:
        if key == '1':
            leds[0].value(1)
        elif key == '2':
            leds[1].value(1)
        elif key == '3':
            leds[2].value(1)
        elif key == '4':
            leds[3].value(1)
        elif key == '5':
            leds[4].value(1)
        elif key == '6':
            leds[5].value(1)
        elif key == '7':
            leds[6].value(1)
        elif key == '8':
            leds[7].value(1)
        elif key == '9':
            for l in range(8):
                leds[l].value(0)

    utime.sleep_ms(50)
