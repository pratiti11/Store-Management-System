from database import conn, cursor


def add_product():
    name = input("Product Name: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))

    cursor.execute(
        "INSERT INTO products(name,price,quantity) VALUES(?,?,?)",
        (name, price, quantity)
    )

    conn.commit()
    print("Product added successfully")


def view_products():
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()

    print("\nInventory\n")
    print("ID | Name | Price | Stock")

    for r in rows:
        print(r)


def update_stock():
    pid = int(input("Enter Product ID: "))
    qty = int(input("Enter New Quantity: "))

    cursor.execute(
        "UPDATE products SET quantity=? WHERE id=?",
        (qty, pid)
    )

    conn.commit()
    print("Stock Updated")


def delete_product():
    pid = int(input("Enter Product ID to delete: "))

    cursor.execute(
        "DELETE FROM products WHERE id=?",
        (pid,)
    )

    conn.commit()
    print("Product Deleted Successfully")