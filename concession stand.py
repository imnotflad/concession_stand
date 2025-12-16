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

def add_item(order):
    price = menu.get(order)
    cart.append(order)
    global total
    total += price
    print(f"\nAdded {order} for ${price:.2f}. Current total: ${total:.2f}") 

def current_cart():
    if cart:
        print("\nYour shopping cart:")
        for item in cart:
            print(f"- {item}: ${menu.get(item):.2f}")
        print(f"Current total: ${total:.2f}")
    else:
        print("\nYour shopping cart is empty!")
        
def remove_loop():
    while True:
        item_to_remove = input("\nEnter the name of the item to remove ('q' to quit remove mode): ").lower()
        if item_to_remove != "q":
            remove_item(item_to_remove)
        else:
            break
        
def remove_item(item_to_remove):
    if item_to_remove in cart:
        removed_price = menu.get(item_to_remove)
        cart.remove(item_to_remove)
        global total
        total -= removed_price
        print(f"\nRemoved {item_to_remove} for ${removed_price:.2f}. Current total: ${total:.2f}")
    else:
        print(f"\n{item_to_remove} is not in your cart.")

print("----CINEMA BAR----")
for item, price in menu.items():
    print(f"{item:8} : ${price:.2f}")
print("------------------")

while True: 
    order = input("\nWhat do you wanna buy? ('check' to see current cart, 'remove' to remove items, 'done' to finish): ").lower()
    match order:
        case _ if order in menu:
            add_item(order)
        case 'remove':
            current_cart()
            remove_loop()
        case 'check':
            current_cart()
        case 'done':
            break
        case _:
            print(f"\nSorry, {order} is not in menu. Try again.")
        
current_cart()  
if cart:
    print("\nThank you for buying!")
else:
    print("\nThanks for coming! Enjoy your time.")