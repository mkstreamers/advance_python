#11. Restaurant Billing System Display a menu with prices and allow users to order multiple items. Calculate the total bill with tax. Use loops for ordering, dictionaries for storing menu, and conditionals for bill logic.
menu = {
    "burger": 100,
    "pizza": 200,
    "pasta": 150,
    "coffee": 80
}

total = 0

while True:
    print("\nMenu:")
    for item, price in menu.items():
        print(item, ":", price)

    choice = input("Enter item to order (or 'done' to finish): ").lower()

    if choice == "done":
        break
    elif choice in menu:
        qty = int(input("Enter quantity: "))
        total += menu[choice] * qty
    else:
        print("Item not available")

tax = total * 0.05
grand_total = total + tax

print("Total:", total)
print("Tax (5%):", tax)
print("Grand Total:", grand_total)