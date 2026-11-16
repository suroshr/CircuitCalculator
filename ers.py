# Finds the total resistance of resistors in series (one after another).

from helpers import get_number_list


def erseries():
    resistors = get_number_list("Enter all the resistors in series (separated by commas): ")
    print(f"Your resistors: {resistors}")

    # In series, you just add all the resistors together
    equivalent = sum(resistors)

    print(f"The equivalent series resistance is: {round(equivalent, 2)} Ω")
    return equivalent
