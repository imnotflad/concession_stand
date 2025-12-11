# Concession stand program

menu = {"pizza" : 3.00,
        "nachos" : 4.50,
        "popcorn" : 6.00,
        "fries" : 2.50,
        "chips" : 1.00,
        "pretzel" : 3.50,
        "soda" : 3.00,
        "lemonade" : 4.25}

cart = []
total = 0
help_mode = False
remove_mode = False

def current_cart():
    if total > 0:
        print("\nYour shopping cart:")
        for cart_item in cart:
            print(f"- {cart_item}: ${menu.get(cart_item):.2f}")
        print(f"Current total: ${total:.2f}")
    else:
        print("Your shopping cart is empty!")

print("----CINEMA BAR----")
for item, price in menu.items():
    print(f"{item:8} : ${price:.2f}")
print("------------------")

while not help_mode: 
    order = input("\nWhat do you wanna buy? ('help' for other options, 'done' to finish): ").lower()
    if order == 'help':
        help_mode = True
        while help_mode:
            current_cart()
            command = input("\nYou can 'remove' to remove items, 'back' to continue shopping and 'done' to finish: ").lower()
            if command == 'remove':  
                remove_mode = True
                while remove_mode:
                    item_to_remove = input("Enter the name of the item to remove ('q' to quit remove mode): ").lower()
                    if item_to_remove in cart:
                        index = cart.index(item_to_remove)
                        removed_price = menu.get(item_to_remove)
                        cart.pop(index)
                        total -= removed_price
                        print(f"\nRemoved {item_to_remove} for ${removed_price:.2f}. Current total: ${total:.2f}")
                        current_cart()
                    elif item_to_remove == "q":
                        remove_mode = False
                    else:
                        print(f"Sorry, {item_to_remove} is not in cart. Try again!")
            elif command == 'back':
                help_mode = False
            elif command == 'done':
                break        
    elif order == 'done':
        break
    elif order in menu:
        price = menu.get(order)
        cart.append(order)
        total += price
        print(f"Added {order} for ${price:.2f}. Current total: ${total:.2f}") 
    else:
        print(f"Sorry, {order} is not in menu. Try again.")
        
if total > 0:
    current_cart()  
    print("Thank you for buying!")
else:
    print("Thanks for coming! Enjoy your time.")