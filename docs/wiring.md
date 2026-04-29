# Wiring and GPIO Mapping (Raspberry Pi Pico W)

This project uses GPIO-number addressing exactly as used by MicroPython `machine.Pin(...)`.

## GPIO Assignments from Firmware

### LED outputs (12 channels)

| LED Index | GPIO |
|---|---:|
| LED0 | GP11 |
| LED1 | GP10 |
| LED2 | GP9 |
| LED3 | GP8 |
| LED4 | GP7 |
| LED5 | GP6 |
| LED6 | GP5 |
| LED7 | GP4 |
| LED8 | GP3 |
| LED9 | GP2 |
| LED10 | GP28 |
| LED11 | GP27 |

### Keypad matrix

#### Rows (outputs)

| Row | GPIO |
|---|---:|
| R0 | GP26 |
| R1 | GP22 |
| R2 | GP21 |
| R3 | GP20 |

#### Columns (inputs, `PULL_DOWN`)

| Column | GPIO |
|---|---:|
| C0 | GP19 |
| C1 | GP18 |
| C2 | GP17 |
| C3 | GP16 |

## Connection Guidance

- Keypad rows connect to `GP26, GP22, GP21, GP20`.
- Keypad columns connect to `GP19, GP18, GP17, GP16`.
- Each LED anode/cathode path must include a resistor.
- Use common GND reference between keypad and LED network.

## Wokwi Tips

- Ensure keypad pin labels (R1..R4, C1..C4) are mapped in row/column order consistent with firmware.
- If a key appears remapped, verify row/column ordering in `diagram.json` against `keys[][]` matrix in code.

## Real Hardware Tips

- Avoid floating inputs: firmware already uses `machine.Pin.PULL_DOWN` for columns.
- Keep wiring short and clean to reduce ghost/noise on matrix scans.
