"""
Program that calculates the total cost of items
"""

DISCOUNT_THRESHOLD = 100
DISCOUNT_RATE = 0.1

total_cost = 0
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
for items in range(1, number_of_items + 1):
    item_price = float(input("Price of item: "))
    total_cost += item_price
if total_cost > DISCOUNT_THRESHOLD:
    discount = total_cost * DISCOUNT_RATE
    total_cost -= discount
print(f"Total price for {number_of_items} items is ${total_cost:.2f}")
