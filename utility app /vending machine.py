# The inventory stored in dictionary
inventory = {
    'A1': {'name': 'Cheetos', 'price': 2.5, 'stock': 15},
    'B2': {'name': 'Oreos', 'price': 3.0, 'stock': 18},
    'C3': {'name': 'Mountain Dew', 'price': 1.75, 'stock': 10},
    'D4': {'name': 'Chicken sandwhich', 'price': 4.0, 'stock': 16},
    'E5': {'name': 'Snickers', 'price': 2.25, 'stock': 15},
    'F6': {'name': 'Sting', 'price': 5.0, 'stock': 10},
    'G7': {'name': 'Butterscotch ice cream', 'price': 3.5, 'stock': 15},
}

def display_inventory():
    """
    Displaying the items in the vending machine with their code, name, price, and stock.
    """
    print("\n========================================")
    print("🍰🍪🧁🍬🍨 𝓿𝓮𝓷𝓭𝓲𝓷𝓰 𝓶𝓪𝓬𝓱𝓲𝓷𝓮  🥧🎂🍦🍭🍩!")
    print("========================================")
    print("Code   Item              Price (AED)   Stock")
    for code, item in inventory.items():
        print(f"{code:<6} {item['name']:<18} {item['price']:<12} {item['stock']}")
    print("========================================")

def process_payment(code):
    """
    Handles the payment process for the selected item.
    """
    item = inventory[code]
    print(f"You selected: {item['name']} (Price: {item['price']} AED)")

    while True:
        try:
            amount_paid = float(input("Please insert the shown amount: "))
            if amount_paid >= item['price']:
                change = amount_paid - item['price']
                if change > 0:
                    print(f"Here is your change: {change:.2f} AED.")
                print(f"Have fun with {item['name']}! 😊")
                inventory[code]['stock'] -= 1  #  To reduce stock by 1
                break
            else:
                print("Insufficient funds. Your payment will be refunded.😢")
                break
        except ValueError:
            print("Invalid input. Please enter a valid amount.😊")

def vending_machine():
    """
    Main vending machine function.
    """
    while True:
        display_inventory()  # To show items in vending machine

        # To ask user to put code for the iteam 
        item_code = input("Enter the code (e.g., A1): ").strip().upper()

        if item_code in inventory:  # check the code 
            if inventory[item_code]['stock'] > 0:  # To check if the item is in stock
                process_payment(item_code)  # Processing payment for the item
            else:
                print(f"Sorry, {inventory[item_code]['name']} is out of stock.😢")
        else:
            print("Invalid  code. Try again.😢")

        # For the user if need anything else 
        anything_else = input("Would you like anything else ? (yes/no): ").strip().lower()
        if anything_else != 'yes':
            print("\nThank you for using the vending machine.Have a great day.🌟")
            break

# To function vending machine 
vending_machine()
