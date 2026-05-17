users = {
    "user@gmail.com": "1234"
}

restaurants = {
    "Pizza Hut": {
        "Chicken Pizza": 1200,
        "Cheese Pizza": 1000,
        "Zinger Burger": 500
    },
    "KFC": {
        "Zinger Burger": 650,
        "Chicken Bucket": 1800,
        "Fries": 300
    },
    "McDonalds": {
        "Big Mac": 700,
        "McChicken": 650,
        "Fries": 250
    }
}

cart = []
current_user = ""
current_restaurant = ""


def login_required():

    if current_user == "":
        print("\nAccess Denied")
        print("Please Login First")
        return False

    return True


def register():

    print("\n========== USER REGISTRATION ==========")

    email = input("Enter Email: ")
    password = input("Enter Password: ")

    if email in users:

        print("\nError: Account Already Exists")

    elif len(password) < 4:

        print("\nError: Password Must Be At Least 4 Characters")

    else:

        users[email] = password
        print("\nRegistration Successful")


def login():

    global current_user

    print("\n========== LOGIN SYSTEM ==========")

    if current_user != "":

        print("\nError: User Already Logged In")
        return

    email = input("Enter Email: ")
    password = input("Enter Password: ")

    if email == "" or password == "":

        print("\nError: Fields Cannot Be Empty")

    elif email not in users:

        print("\nError: Account Not Found")

    elif users[email] != password:

        print("\nError: Incorrect Password")

    else:

        current_user = email

        print("\nLogin Successful")
        print("Welcome:", current_user)


def logout():

    global current_user
    global cart
    global current_restaurant

    print("\n========== LOGOUT SYSTEM ==========")

    if current_user == "":

        print("\nError: No User is Logged In")

    else:

        print("\nUser Logged Out Successfully")

        current_user = ""

        cart.clear()

        current_restaurant = ""

        print("All User Access Removed")


def show_restaurants():

    if login_required() == False:
        return

    print("\n========== AVAILABLE RESTAURANTS ==========")

    count = 1

    for restaurant in restaurants:

        print(count, ".", restaurant)

        count += 1


def search_restaurant():

    global current_restaurant

    if login_required() == False:
        return

    print("\n========== SEARCH RESTAURANT ==========")

    search = input("Enter Restaurant Name: ")

    found = False

    for restaurant in restaurants:

        if search.lower() in restaurant.lower():

            print("\nRestaurant Found:", restaurant)

            current_restaurant = restaurant

            print("\nFood Menu:")

            for food, price in restaurants[restaurant].items():

                print(food, "- Rs.", price)

            found = True

    if found == False:

        print("\nRestaurant Not Found")


def order_food():

    if login_required() == False:
        return

    print("\n========== ORDER FOOD ==========")

    if current_restaurant == "":

        print("\nError: Please Search Restaurant First")
        return

    print("\nSelected Restaurant:", current_restaurant)

    print("\nAvailable Food Items:")

    for food, price in restaurants[current_restaurant].items():

        print(food, "- Rs.", price)

    food_item = input("\nEnter Food Item Name: ")

    if food_item not in restaurants[current_restaurant]:

        print("\nError: Food Item Not Available")
        return

    quantity = input("Enter Quantity: ")

    if quantity.isdigit() == False:

        print("\nError: Invalid Quantity")
        return

    quantity = int(quantity)

    if quantity <= 0:

        print("\nError: Quantity Must Be Greater Than 0")
        return

    total_price = restaurants[current_restaurant][food_item] * quantity

    item = {
        "restaurant": current_restaurant,
        "food": food_item,
        "quantity": quantity,
        "price": total_price
    }

    cart.append(item)

    print("\nFood Ordered Successfully")
    print("Added to Cart")


def view_cart():

    if login_required() == False:
        return

    print("\n========== VIEW CART ==========")

    if len(cart) == 0:

        print("\nCart is Empty")

    else:

        total_bill = 0
        count = 1

        for item in cart:

            print("\nItem", count)

            print("Restaurant:", item["restaurant"])
            print("Food Item:", item["food"])
            print("Quantity:", item["quantity"])
            print("Price: Rs.", item["price"])

            total_bill += item["price"]

            count += 1

        print("\nTotal Bill = Rs.", total_bill)


def remove_cart_item():

    if login_required() == False:
        return

    print("\n========== REMOVE CART ITEM ==========")

    if len(cart) == 0:

        print("\nError: Cart is Empty")
        return

    remove_item = input("Enter Food Item Name to Remove: ")

    found = False

    for item in cart:

        if item["food"].lower() == remove_item.lower():

            cart.remove(item)

            print("\nItem Removed Successfully")

            found = True

            break

    if found == False:

        print("\nError: Item Not Found")


def payment():

    if login_required() == False:
        return

    print("\n========== ONLINE PAYMENT ==========")

    if len(cart) == 0:

        print("\nError: Cart is Empty")
        return

    total_amount = 0

    for item in cart:

        total_amount += item["price"]

    print("\nTotal Amount = Rs.", total_amount)

    card_number = input("Enter 16 Digit Card Number: ")
    card_holder = input("Enter Card Holder Name: ")
    cvv = input("Enter 3 Digit CVV: ")

    if len(card_number) != 16:

        print("\nError: Invalid Card Number")

    elif card_number.isdigit() == False:

        print("\nError: Card Number Must Contain Digits Only")

    elif len(cvv) != 3:

        print("\nError: Invalid CVV")

    elif cvv.isdigit() == False:

        print("\nError: CVV Must Contain Digits Only")

    elif card_holder == "":

        print("\nError: Card Holder Name Cannot Be Empty")

    else:

        print("\nPayment Successful")
        print("Order Confirmed")


def order_tracking():

    if login_required() == False:
        return

    print("\n========== ORDER TRACKING ==========")

    if len(cart) == 0:

        print("\nError: No Active Orders Found")
        return

    print("\nCurrent Order Status")

    print("1. Order Confirmed")
    print("2. Restaurant Preparing Food")
    print("3. Rider Picked Up Order")
    print("4. Order On The Way")
    print("5. Order Delivered")

    status = input("\nEnter Status Number: ")

    if status == "1":

        print("\nStatus: Order Confirmed")

    elif status == "2":

        print("\nStatus: Food is Being Prepared")

    elif status == "3":

        print("\nStatus: Rider Picked Up Your Order")

    elif status == "4":

        print("\nStatus: Your Order is On The Way")

    elif status == "5":

        print("\nStatus: Order Delivered Successfully")

    else:

        print("\nError: Invalid Status")


def main():

    while True:

        print("\n")
        print("=================================================")
        print("         FOODPANDA FOOD DELIVERY SYSTEM")
        print("=================================================")
        print("1. Register")
        print("2. Login")
        print("3. Logout")
        print("4. Show Restaurants")
        print("5. Search Restaurant")
        print("6. Order Food")
        print("7. View Cart")
        print("8. Remove Cart Item")
        print("9. Online Payment")
        print("10. Order Tracking")
        print("11. Exit")
        choice = input("\nEnter Your Choice: ")
        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            logout()
        elif choice == "4":
            show_restaurants()
        elif choice == "5":
            search_restaurant()
        elif choice == "6":
            order_food()
        elif choice == "7":
            view_cart()
        elif choice == "8":
            remove_cart_item()
        elif choice == "9":
            payment()
        elif choice == "10":
            order_tracking()
        elif choice == "11":
            print("\nSystem Closed Successfully")
            break
        else:

            print("\nError: Invalid Menu Choice")

if __name__ == "__main__":
    main()