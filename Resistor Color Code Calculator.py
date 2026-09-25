# Resistor Color Code Calculator

print("===== RESISTOR COLOR CODE CALCULATOR =====")

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

multipliers = {
    "black": 1,
    "brown": 10,
    "red": 100,
    "orange": 1000,
    "yellow": 10000,
    "green": 100000,
    "blue": 1000000,
    "violet": 10000000,
    "grey": 100000000,
    "white": 1000000000
}

# Get color inputs
band1 = input("Enter 1st band color: ").lower()
band2 = input("Enter 2nd band color: ").lower()
band3 = input("Enter multiplier band color: ").lower()

# Check valid colors
if band1 in colors and band2 in colors and band3 in multipliers:

    resistance = (colors[band1] * 10 + colors[band2]) * multipliers[band3]

    print("\n===== RESULT =====")
    print("Resistance =", resistance, "Ω")

    # Convert to suitable unit
    if resistance >= 1000000:
        print("Resistance =", resistance / 1000000, "MΩ")
    elif resistance >= 1000:
        print("Resistance =", resistance / 1000, "kΩ")

else:
    print("Invalid color entered!")