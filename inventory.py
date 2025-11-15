item_names = []
item_prices = {}

print("===== INVENTORY MENU =====")
print("[1] Add Item")
print("[2] Update Price")
print("[3] Exit")

while True:
    choicee = input("Choice: ")

    if choicee == "1":
        name = input("Enter item name: ")

        if name in item_names:
            print("Item already exists in the inventory.\n")
        else:
            try:
                price = float(input("Enter price: "))
                item_names.append(name)
                item_prices[name] = price
                print("Item added successfully!\n")
            except ValueError:
                print("Invalid price.\n")

    elif choicee == "2":
        name = input("Enter item name to update: ")

        if name in item_names:
            try:
                new_price = float(input("Enter new price: "))
                item_prices[name] = new_price
                print("Price updated successfully!\n")
            except ValueError:
                print("Invalid price.\n")
        else:
            print("Item not found in the inventory.\n")

    elif choicee == "3":
        print("Exiting system...")
        break

    else:
        print("Invalid choice.\n")
