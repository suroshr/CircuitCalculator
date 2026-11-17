# Finds the power used (in watts) when you know two of:
# voltage, current, or resistance.

from helpers import get_number


def power():
    known = input("What two components do you know: \n"
                  "1: Voltage and Current\n"
                  "2: Resistance and Current\n"
                  "3: Voltage and Resistance\n"
                  "Enter your choice: ").strip()

    # Know voltage and current: P = V x I
    if known == "1":
        current = get_number("Current (A): ")
        voltage = get_number("Voltage (V): ")
        result = voltage * current

    # Know resistance and current: P = I² x R
    elif known == "2":
        resistance = get_number("Resistance (Ω): ")
        current = get_number("Current (A): ")
        result = resistance * current**2

    # Know voltage and resistance: P = V² / R
    elif known == "3":
        voltage = get_number("Voltage (V): ")
        resistance = get_number("Resistance (Ω): ")
        # Can't divide by a resistance of 0
        if resistance == 0:
            print("Error: Resistance cannot be zero.\n")
            return
        result = voltage**2 / resistance

    # They typed something that's not 1, 2 or 3, so stop here
    else:
        print("Invalid Input\n")
        return

    # All three options show the answer the same way, so it's printed once here
    print(f"Power Dissipated: {round(result, 2)} Watts\n")
