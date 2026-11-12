# Circuit Calculator

A command-line calculator for **resistor color codes**, **Ohm's Law**, **series and parallel resistance**, **current and voltage dividers**, and **power**.

## Features

- Read a 4-band resistor's value and tolerance from its colors
- Solve Ohm's Law for voltage, current or resistance
- Find the total resistance of resistors in series or in parallel
- Find the current through one resistor with a current divider
- Find the voltage across one resistor with a voltage divider
- Find the power dissipated from any two of voltage, current or resistance
- Handles bad input without crashing (letters, empty input, invalid colors, dividing by zero)
- Ignores extra spaces, capital letters and trailing commas

## How to run

You need Python 3.6 or newer.

```bash
python CircuitCalculator.py
```

Then pick a calculator from the menu by typing its number (1 to 7) and follow the prompts.

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
Enter your choice: 2
What do you want to find?
1: Resistance
2: Current
3: Voltage
Enter your choice: 2
Resistance (Ω): 4
Voltage (V): 12
Current: 3.0 A

Do you have any other calculations? (yes/no): yes

How can I help you today?
...
Enter your choice: 1
What color is the first band? yellow
What color is the second band? violet
What color is the third band? red
What color is the fourth band? gold
Resistance: 4700 ohms ±5%

Do you have any other calculations? (yes/no): no
Goodbye!
```

## How it works

The main file shows the menu. The menu is a dictionary that links each number to a function in its own file:

```
menu choice  ->  dictionary  ->  calculator function
```

| # | Calculator | File | Function |
|---|---|---|---|
| 1 | Resistor color code | `ResistorCalculator.py` | `resistor_calculator` |
| 2 | Ohm's Law | `OhmsLaw.py` | `ohms_law` |
| 3 | Series resistance | `ers.py` | `erseries` |
| 4 | Parallel resistance | `erp.py` | `erparallel` |
| 5 | Current divider | `CurrentDivider.py` | `cd` |
| 6 | Voltage divider | `VoltageDivider.py` | `vd` |
| 7 | Power | `Power.py` | `power` |

Adding a new calculator only means writing its file and adding one line to the menu.

**Shared code:**
- **`helpers.py`** has the functions that ask for numbers. Every calculator uses them, so bad input is handled the same way everywhere.
- **The dividers reuse the series and parallel files.** The current divider gets the total resistance from `erp.py`, and the voltage divider gets it from `ers.py`.
- **One function reads all 4 color bands.** `ask_color` takes the band and the list of valid colors for it, instead of having a separate function for each band.

**Formulas:**
- **Ohm's Law:** `V = I × R`
- **Series:** `R_total = R1 + R2 + ...`
- **Parallel:** `R_total = 1 / (1/R1 + 1/R2 + ...)`
- **Current divider:** `I_x = I_total × (R_total / R_x)`
- **Voltage divider:** `V_x = V_total × (R_x / R_total)`
- **Power:** `P = V × I = I² × R = V² / R`

## Flowchart

![Flowchart](CircuitCalculator_FlowChart.png)

A PDF version is in [`CircuitCalculator_FlowChart.pdf`](CircuitCalculator_FlowChart.pdf).

## Notes

- Answers are rounded to 2 decimals, so very small values (like 0.004 A) show as `0.0`. Enter values in units that keep the answer above 0.01.
- The dividers don't check that the resistor you pick is one of the resistors you entered. Make sure it matches one from your list.
- The resistor calculator only works with 4-band resistors.

## What I learned

- Splitting a program into separate files and importing them
- Using a dictionary to link menu choices to functions instead of a long `if/elif` chain
- Using `try/except` to handle bad input instead of letting the program crash
- Writing one function that handles many cases instead of copying the same code
- Turning a line like `100, 200, 300` into a list of numbers

## Ideas for later

- Show the current or voltage for every resistor at once in the dividers
- Support 5-band and 6-band resistors
- Show results with unit prefixes like kΩ and mA
- Build a simple window app instead of the terminal
