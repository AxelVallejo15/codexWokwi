# Pico W Keypad-to-LED Controller (MicroPython)

This repository is organized for a **Raspberry Pi Pico W (RP2040)** project that scans a 4x4 matrix keypad and drives 12 external LEDs according to key presses.

> Core behavior is intentionally unchanged: the firmware scans keypad rows/columns and sets LED outputs based on the pressed key.

## Repository Structure

```text
.
├── README.md
├── src/
│   └── main.py
├── lib/
└── docs/
    ├── architecture.md
    └── wiring.md
```

- `src/main.py`: main MicroPython firmware entry point.
- `lib/`: optional reusable MicroPython modules.
- `docs/wiring.md`: wiring and GPIO mapping.
- `docs/architecture.md`: firmware architecture and runtime flow.

## Features

- 4x4 matrix keypad scanning using row drive + column sensing.
- 12 independent LED outputs on Pico W GPIO pins.
- Deterministic polling loop suitable for Wokwi simulation and real hardware.

## Components (from project scope / Wokwi hardware intent)

- 1x Raspberry Pi Pico W
- 1x 4x4 matrix keypad
- 12x LEDs
- 12x current-limiting resistors (typically 220Ω to 1kΩ)
- Hook-up wires / breadboard

## Quick Start (Wokwi)

1. Create/import a Raspberry Pi Pico W project in Wokwi.
2. Add your `diagram.json` and copy firmware to `src/main.py` (or `main.py` at project root for direct simulation).
3. Run simulation.
4. Press keypad keys and observe LED output behavior.

## Quick Start (Real Pico W Hardware)

1. Install MicroPython on Pico W:
   - Hold `BOOTSEL`, plug USB, mount as `RPI-RP2`.
   - Flash latest Pico W MicroPython UF2.
2. Connect keypad + LEDs as documented in [`docs/wiring.md`](docs/wiring.md).
3. Copy firmware to board as `main.py` (or `boot.py` loader plus `src/main.py` import strategy).
4. Reset board and test key-to-LED mapping.

## Flashing / Deployment Options

### Option A: Thonny (recommended)

- Interpreter: **MicroPython (Raspberry Pi Pico)**
- Save `src/main.py` to device as `/main.py`

### Option B: `mpremote`

```bash
mpremote connect auto fs cp src/main.py :main.py
mpremote connect auto reset
```

## Notes

- Pico W pin numbers in code are **GPIO numbers**, not physical header pin indices.
- Keep all LED circuits current-limited with series resistors.
