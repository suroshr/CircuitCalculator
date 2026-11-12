# Asks for one number and keeps asking until they type a real number
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


# Asks for numbers separated by commas and keeps asking until they're all real numbers
def get_number_list(prompt):
    while True:
        rawinput = input(prompt)

        # Turn each piece into a number, skipping empty spots
        try:
            numbers = [float(r) for r in rawinput.split(",") if r.strip()]
        except ValueError:
            print("Invalid input. Use numbers separated by commas.")
            continue

        # Make sure they typed at least one number
        if numbers:
            return numbers
        print("Please enter at least one number.")
