# Reads the color bands on a 4-band resistor and tells you its value.

# Bands 1 and 2: each color stands for a digit
colors = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9
}

# Band 3: what to multiply the first two digits by
multipliers = {
    "black": 10**0,
    "brown": 10**1,
    "red": 10**2,
    "orange": 10**3,
    "yellow": 10**4,
    "green": 10**5,
    "blue": 10**6,
    "violet": 10**7,
    "grey": 10**8,
    "white": 10**9,
    "gold": 10**-1,
    "silver": 10**-2
}

# Band 4: how accurate the resistor is
tolerances = {
    "brown": "±1%",
    "red": "±2%",
    "green": "±0.5%",
    "blue": "±0.25%",
    "violet": "±0.1%",
    "grey": "±0.05%",
    "gold": "±5%",
    "silver": "±10%"
}


# Asks for one band's color and keeps asking until it's in the right list.
# This one function handles all 4 bands, instead of writing 4 almost identical ones.
def ask_color(band, options):
    color = input(f"What color is the {band} band? ").strip().lower()

    while color not in options:
        print("Invalid color. Try again.")
        color = input(f"What color is the {band} band? ").strip().lower()

    return options[color]


# Asks for all 4 bands and shows the resistance
def resistor_calculator():
    first = ask_color("first", colors)
    second = ask_color("second", colors)
    multiplier = ask_color("third", multipliers)
    tol = ask_color("fourth", tolerances)

    # Put the first two digits side by side, then multiply
    total = (first * 10 + second) * multiplier

    print(f"Resistance: {total:g} ohms {tol}")
