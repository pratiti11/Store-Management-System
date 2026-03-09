from database import conn, cursor
from datetime import datetime


def view_products():

    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()

    print("\nAvailable Products\n")
    print("ID | Name | Price | Stock")

    for r in rows:
        print(r)


def buy_product(store_name):

    pid = int(input("Enter Product ID: "))
    qty = int(input("Enter Quantity: "))

    cursor.execute(
        "SELECT name,price,quantity FROM products WHERE id=?",
        (pid,)
    )

    product = cursor.fetchone()

    if product is None:
        print("Product not found")
        return

    name, price, stock = product

    if qty > stock:
        print("Not enough stock")
        return

    total = price * qty

    date = datetime.now().strftime("%d-%m-%Y %H:%M")

    print("\n================================")
    print("        ", store_name)
    print("================================")
    print("Date:", date)
    print("--------------------------------")
    print("Product:", name)
    print("Price:", price)
    print("Quantity:", qty)
    print("--------------------------------")
    print("TOTAL:", total)
    print("================================")
    print("Thank you for shopping!")
    print("================================")

    new_stock = stock - qty

    cursor.execute(
        "UPDATE products SET quantity=? WHERE id=?",
        (new_stock, pid)
    )

    cursor.execute(
        "INSERT INTO sales(product_name,quantity,total_price) VALUES(?,?,?)",
        (name, qty, total)
    )

    conn.commit()

    print("\nPurchase Successful")