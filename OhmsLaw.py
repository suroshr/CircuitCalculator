from helpers import get_number

def ohms_law():
    unknown = input("What do you want to find? \n"
                    "1: Resistance \n"
                    "2: Current \n"
                    "3: Voltage\n"
                    "Enter your choice: ").strip()

    # Find resistance: R = V / I
    if unknown == "1":
        current = get_number("Current (A): ")
        voltage = get_number("Voltage (V): ")
        # Can't divide by a current of 0
        if current == 0:
            print("Error: Current cannot be zero.\n")
            return
        print(f"Resistance: {round(voltage / current, 2)} Ω\n")

    # Find current: I = V / R
    elif unknown == "2":
        resistance = get_number("Resistance (Ω): ")
        voltage = get_number("Voltage (V): ")
        # Can't divide by a resistance of 0
        if resistance == 0:
            print("Error: Resistance cannot be zero.\n")
            return
        print(f"Current: {round(voltage / resistance, 2)} A\n")

    # Find voltage: V = I x R
    elif unknown == "3":
        current = get_number("Current (A): ")
        resistance = get_number("Resistance (Ω): ")
        print(f"Voltage: {round(current * resistance, 2)} V\n")

    # They typed something that's not 1, 2 or 3
    else:
        print("Invalid Input\n")
