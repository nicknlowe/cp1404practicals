"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

STATE_CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"}
print(STATE_CODE_TO_NAME)

state_code = input("Enter short state: ").upper()
while state_code != "":
    if state_code in STATE_CODE_TO_NAME:
        print(state_code, "is", STATE_CODE_TO_NAME[state_code])
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()

for states in STATE_CODE_TO_NAME:
    print(f"{states:<3} is {STATE_CODE_TO_NAME[states]}")
