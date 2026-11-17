# For resistors in series: finds how much of the total voltage
# lands on one resistor.

import ers
from helpers import get_number


def vd():
    # Get the total series resistance first
    equiv_resistance = ers.erseries()

    # Stop if the total is 0, since the math would break
    if equiv_resistance == 0:
        print("Error: Total resistance cannot be zero.")
        return

    resistor = get_number("What is the resistor of which you want to find the voltage: ")
    voltage = get_number("What is the total voltage: ")

    # Voltage on the resistor = total voltage x (that resistor / total resistance)
    voltx = voltage * (resistor / equiv_resistance)

    print(f"The voltage for the resistor is: {round(voltx, 2)} V")
