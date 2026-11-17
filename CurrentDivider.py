# For resistors in parallel: finds how much of the total current
# goes through one resistor.

import erp
from helpers import get_number


def cd():
    # Get the total parallel resistance first
    equiv_resistance = erp.erparallel()

    # Stop if the parallel calculation had an error
    if equiv_resistance is None:
        return

    resistor = get_number("What is the resistor of which you want to find the current: ")
    current = get_number("What is the total current: ")

    # A 0 Ω resistor would break the math
    if resistor == 0:
        print("Error: Target resistor cannot be zero.")
        return

    # Current in the resistor = total current x (total resistance / that resistor)
    currentx = current * (equiv_resistance / resistor)

    print(f"The current for the resistor is: {round(currentx, 2)} A")
