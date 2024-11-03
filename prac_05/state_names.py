"""
CP1404/CP5632 Practical
State names in a dictionary
"""

STATE_CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory",
                      "WA": "Western Australia", "ACT": "Australian Capital Territory", "VIC": "Victoria",
                      "TAS": "Tasmania", "SA": "South Australia"}
print(STATE_CODE_TO_NAME)

state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        print(state_code, "is", STATE_CODE_TO_NAME[state_code])
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()

for state in STATE_CODE_TO_NAME:
    print(f"{state:<3} is {STATE_CODE_TO_NAME[state]}")
