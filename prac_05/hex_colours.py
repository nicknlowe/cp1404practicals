"""
CP1404/CP5632 Practical
Hex colours in a dictionary
"""

COLOURS_TO_HEX = {"aliceblue": "#f0f8ff", "aqua": "#00ffff", "burgundy": "#800020", "cream": "#fffdd0",
                  "denim": "#1560bd", "firebrick": "#b22222", "frostbite": "#e936a7", "goldenrod": "#daa520",
                  "gray": "#bebebe", "indigo": "#4b0082"}

colour = input("Enter a colour: ").lower()
while colour != "":
    try:
        print(f"The hex for {colour} is {COLOURS_TO_HEX[colour]}")
    except KeyError:
        print(f"Oops, I don't think I have that colour")
    colour = input("Enter a colour: ").lower()
