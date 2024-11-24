"""
CP1404/CP5632 Practical
Taxi Simulator that utilises the Taxi and SilverServiceTaxi classes
"""

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Taxi Simulator program to select taxis, drive it and calculate the total bill."""
    taxis = [Taxi('Prius', 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    total_bill = 0
    current_taxi = None
    print("Let's drive!")
    print(MENU)
    choice = input("Choose a menu option: ").lower()
