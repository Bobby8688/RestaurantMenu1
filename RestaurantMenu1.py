#RestaurantMenu1.py
import time

menu = {
    "Burger": 199,
    "Pizza": 299,
    "Salad": 399,
    "Soda": 169,
    "Coffee": 119
}

def menu2():
    print("-" * 50)
    print("MENU")
    print("-" * 50)
    for key, item in menu.items():
        print("{}\t{}".format(key, item))

def user_input():
    print("-" * 50)
    print("HOME")
    print("-" * 50)
    print("\n1. View Menu")
    print("2. Add Items to Cart")
    print("3. Reset Cart")
    choose = int(input("Enter your choice: "))
    
    if choose == 1:
        print("Loading Menu...")
        time.sleep(2)
        menu2()
    elif choose == 2:
        cart1()
    elif choose == 3:
        cart.clear()
        print("Cart is Reset")
    else:
        print("Invalid choice. Please try again.")

cart=[]

def cart1():
    item = input("Enter the Item to add to cart: ")
    if item in menu:
        cart.append(item)
        print("{} is Added to the Cart".format(item))
    else:
        print("{} is unavailable".format(item))
    return cart

user_input()
cart1()