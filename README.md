# Circuit Calculator

A simple Python calculator for basic circuit problems. Pick a calculation from the menu, type in your values, and it gives you the answer.

## How to use

* Pick a calculator by typing its number (1 to 7).
* Type in the values it asks for.
* It shows the answer, then asks if you want to do another one.

## What it does

* Finds a resistor's value and tolerance from its 4 color bands
* Solves Ohm's Law for voltage, current, or resistance
* Finds the total resistance of resistors in series or in parallel
* Finds the current through one resistor with a current divider
* Finds the voltage across one resistor with a voltage divider
* Finds the power used when you know any two of voltage, current, or resistance
* If you type letters or leave it empty, it tells you and asks again
* If a value would make it divide by zero, it tells you instead of crashing
* Keeps asking until you type a real color for the resistor bands
* Ignores extra spaces, capital letters, and a trailing comma

## How to run it

You need Python 3 installed.

```
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
What is the total current: abc
Invalid input. Please enter a number.
What is the total current: 6
The current for the resistor is: 3.27 A

Do you have any other calculations? (yes/no): no
Goodbye!
```

## How it works

1. `CircuitCalculator.py` shows the menu and waits for a choice.
2. The menu is a dictionary that links each number to the right calculator, so the choice runs that calculator's function.
3. Each calculator lives in its own file (`OhmsLaw.py`, `Power.py`, `ers.py`, and so on).
4. Every number the user types goes through `helpers.py`, which keeps asking until it gets a real number.
5. The divider calculators reuse the series and parallel files to get the total resistance first.
6. After each answer, a `while` loop asks if the user wants another calculation, and stops when they say no.

## Flowchart

[View the flowchart (PDF)](CircuitCalculator_FlowChart.pdf)

## What I learned

* How to split a program into different files and import them
* How to use dictionaries to match colors to numbers and menu choices to functions
* How to use `try/except` so bad input doesn't crash the program
* How to write one function that works for many cases instead of copying the same code
* How to turn a line of text like `100, 200, 300` into a list of numbers
* What `if __name__ == "__main__":` does

## Ideas for later

* Show the current or voltage for every resistor at once in the dividers
* Support 5-band and 6-band resistors
* Show results with unit prefixes like kΩ and mA
* Build a simple window app instead of the terminal
