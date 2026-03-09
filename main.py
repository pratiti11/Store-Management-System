from database import create_tables
import owner
import customer

# create database tables
create_tables()

STORE_NAME = input("Enter Store Name: ")
OWNER_PASSWORD = "1234@abcd"

while True:

    print("\n=================================")
    print("   WELCOME TO", STORE_NAME)
    print("=================================")

    print("1 Owner Panel")
    print("2 Customer")
    print("3 Exit")

    choice = input("Enter choice: ")

    # OWNER PANEL
    if choice == "1":

        password = input("Enter Owner Password: ")

        if password != OWNER_PASSWORD:
            print("Wrong Password")
            continue

        print("\nWelcome Owner")

        while True:

            print("\nOWNER MENU")
            print("1 Add Product")
            print("2 View Inventory")
            print("3 Update Stock")
            print("4 Delete Product")
            print("5 Back")

            c = input("Enter choice: ")

            if c == "1":
                owner.add_product()

            elif c == "2":
                owner.view_products()

            elif c == "3":
                owner.update_stock()

            elif c == "4":
                owner.delete_product()

            elif c == "5":
                break

    # CUSTOMER PANEL
    elif choice == "2":

        while True:

            print("\nCUSTOMER MENU")
            print("1 View Products")
            print("2 Buy Product")
            print("3 Back")

            c = input("Enter choice: ")

            if c == "1":
                customer.view_products()

            elif c == "2":
                customer.buy_product(STORE_NAME)

            elif c == "3":
                break

    elif choice == "3":
        print("Exiting system...")
        break