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
status = 0

print("----CINEMA BAR----")
for item, price in menu.items():
    print(f"{item:8} : ${price:.2f}")
print("------------------")

while status == 0: 
    order = input("\nWhat do you wanna buy? ('help' for other options, 'done' to finish): ")  
    if order.lower() == 'help':
        status += 1
        while status == 1:
            command = input("\nYou can 'remove' to remove items, 'check' to check current cart and total, 'back' to continue shopping and 'done' to finish: ")
            if command.lower() == 'remove':
                print("\nYour shopping cart:")
                for cart_item in cart:
                    print(f"- {cart_item}: ${menu.get(cart_item):.2f}")
                print(f"Current total: ${total:.2f}")    
                item_to_remove = input("Enter the name of the item to remove: ")
                if item_to_remove in cart:
                    index = cart.index(item_to_remove)
                    removed_price = menu.get(item_to_remove)
                    cart.pop(index)
                    total -= removed_price
                    print(f"Removed {item_to_remove} for ${removed_price:.2f}. Current total: ${total:.2f}")
            elif command.lower() == 'check':
                print("\nYour shopping cart:")
                for cart_item in cart:
                    print(f"- {cart_item}: ${menu.get(cart_item):.2f}")
                print(f"Current total: ${total:.2f}")   
            elif command.lower() == 'back':
                status -= 1 
            elif command.lower() == 'done':
                break
           
    elif order.lower() == 'done':
        break
    elif order.lower() in menu:
        price = menu.get(order.lower())
        cart.append(order.lower())
        total += price
        print(f"Added {order.lower()} for ${price:.2f}. Current total: ${total:.2f}") 
    else:
        print(f"Sorry, {order} is not in menu. Try again.")
        
print("\nYour shopping cart:")
for cart_item in cart:
    print(f"- {cart_item}: ${menu.get(cart_item):.2f}")
print(f"Current total: ${total:.2f}")   
print("Thank you for buying!")