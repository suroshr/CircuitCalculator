# Circuit Calculator

A command-line calculator for basic circuit problems, written in Python.
Pick a calculation from the menu, type in your values, and get the answer.

## What it can do

| # | Calculator | What it finds |
|---|------------|---------------|
| 1 | Resistor Color Code | A resistor's value and tolerance from its 4 color bands |
| 2 | Ohm's Law | Voltage, current, or resistance when you know the other two |
| 3 | Series Resistance | Total resistance of resistors in series |
| 4 | Parallel Resistance | Total resistance of resistors in parallel |
| 5 | Current Divider | Current through one resistor in a parallel circuit |
| 6 | Voltage Divider | Voltage across one resistor in a series circuit |
| 7 | Power | Power dissipated, using any two of voltage, current, or resistance |

It also handles mistakes: if you type letters instead of a number, or a value
that would divide by zero, it tells you and asks again instead of crashing.

## How to run it

You need Python 3. No extra libraries are needed.

1. Download or clone this repo.
2. Open a terminal in the project folder.
3. Run:

```bash
python CircuitCalculator.py
```

## Example

```
Welcome to the Circuit Calculator

How can I help you today?
1: Resistance Calculator on Component
2: Ohm's Law
3: Equivalent Resistance in Series
4: Equivalent Resistance in Parallel
5: Current Divider
6: Voltage Divider
7: Power
Enter your choice: 5
Enter all the resistors in parallel (separated by commas): 100, 200, 300
Your resistors: [100.0, 200.0, 300.0]
The equivalent parallel resistance is: 54.55 Ω
What is the resistor of which you want to find the current: 100
What is the total current: 6
The current for the resistor is: 3.27 A

Do you have any other calculations? (yes/no): no
Goodbye!
```

## Formulas used

| Calculation | Formula |
|-------------|---------|
| Ohm's Law | V = I × R |
| Series | R_total = R1 + R2 + ... |
| Parallel | R_total = 1 / (1/R1 + 1/R2 + ...) |
| Current divider | I_x = I_total × (R_total / R_x) |
| Voltage divider | V_x = V_total × (R_x / R_total) |
| Power | P = V × I = I² × R = V² / R |

## Project structure

```
CircuitCalculator.py   Main file: shows the menu and runs the calculator you pick
ResistorCalculator.py  Reads the resistor color bands
OhmsLaw.py             Ohm's Law
ers.py                 Equivalent resistance in series
erp.py                 Equivalent resistance in parallel
CurrentDivider.py      Current divider (uses erp.py)
VoltageDivider.py      Voltage divider (uses ers.py)
Power.py               Power calculations
helpers.py             Shared tools for asking the user for numbers
```

## Future ideas

- Show the current or voltage for every resistor at once in the divider calculators
- Support 5-band and 6-band resistors
- Show results with unit prefixes (kΩ, mA, etc.)
- Add automated tests
- Build a simple graphical interface

## Author

Surosh Rajabi, Electrical Engineering student at Concordia University
