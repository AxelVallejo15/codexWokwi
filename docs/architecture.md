# Firmware Architecture

## Runtime Model

The firmware is a single-loop, polling-based MicroPython application:

1. Initialize LED GPIO pins as outputs and set them LOW.
2. Initialize keypad row GPIO as outputs.
3. Initialize keypad column GPIO as inputs with pulldown.
4. Repeatedly scan keypad with `read_keypad()`.
5. Apply key-to-LED behavior.

## Module/Layout Strategy

- `src/main.py`: executable entrypoint on device.
- `lib/`: reserved for future extraction (e.g., `keypad.py`, `led_bank.py`) without changing functional behavior.

## Core Data Structures

- `led_pins`: ordered list of 12 LED GPIO outputs.
- `row_pins` / `col_pins`: matrix scan pin lists.
- `keys`: 4x4 map from matrix position to symbolic key (`'0'..'9', '*', '#', 'A'..'D'`).

## Keypad Scan Flow

`read_keypad()` drives one row HIGH at a time, then samples each column input:

- If a column reads HIGH, key = `keys[row][col]`.
- The active row is immediately restored LOW before returning.
- If no key is pressed, function returns `None`.

## Behavior Preservation

Repository/documentation updates are designed to preserve firmware logic. Functional behavior should remain tied to the original `main.py` mapping and loop semantics.
