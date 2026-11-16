# Finds the total resistance of resistors in parallel (side by side).

from helpers import get_number_list


def erparallel():
    resistors = get_number_list("Enter all the resistors in parallel (separated by commas): ")
    print(f"Your resistors: {resistors}")

    # Every resistor has to be more than 0 for the math to work
    if any(r <= 0 for r in resistors):
        print("Error: Resistance must be more than zero.")
        return None

    # Add up 1 divided by each resistor, then flip the total
    equivalent = 1 / sum(1 / r for r in resistors)

    print(f"The equivalent parallel resistance is: {round(equivalent, 2)} Ω")
    return equivalent
