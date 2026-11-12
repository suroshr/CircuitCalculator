import ResistorCalculator
import OhmsLaw
import ers
import erp
import Power
import CurrentDivider
import VoltageDivider

# Each menu number, the name shown to the user, and the calculator it runs
menu = {
    "1": ("Resistance Calculator on Component", ResistorCalculator.resistor_calculator),
    "2": ("Ohm's Law", OhmsLaw.ohms_law),
    "3": ("Equivalent Resistance in Series", ers.erseries),
    "4": ("Equivalent Resistance in Parallel", erp.erparallel),
    "5": ("Current Divider", CurrentDivider.cd),
    "6": ("Voltage Divider", VoltageDivider.vd),
    "7": ("Power", Power.power),
}


def main():
    print("Welcome to the Circuit Calculator")

    # Keep showing the menu until the user says they're done
    while True:
        print("\nHow can I help you today?")
        for number, (name, calculator) in menu.items():
            print(f"{number}: {name}")
        choice = input("Enter your choice: ").strip()

        # Run the calculator for that choice, or say the choice wasn't valid
        if choice in menu:
            name, calculator = menu[choice]
            calculator()
        else:
            print("Invalid choice. Pick a number from 1 to 7.")

        # Ask if they want to do another calculation
        repeat = input("\nDo you have any other calculations? (yes/no): ").strip().lower()
        if repeat not in ["yes", "y"]:
            print("Goodbye!")
            break


# Only start the calculator when this file is run directly
if __name__ == "__main__":
    main()
