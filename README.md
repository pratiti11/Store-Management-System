# Store Management & Billing System

A simple **Store Management and Billing System** built using **Python and SQLite**.
The system allows a store owner to manage inventory and customers to purchase products while automatically generating a bill and updating stock.

The store used in this system is **Pratiti Mart**.

---

# Features

## Owner Panel

* Password protected owner login
* Add new products to inventory
* View available products
* Update product stock
* Delete products from inventory

## Customer Panel

* View available products
* Buy products
* Automatic bill generation
* Automatic stock update after purchase

---

# Technologies Used

* Python
* SQLite
* SQL Queries
* Command Line Interface (CLI)

---

# Project Structure

```
store-management-system
│
├── main.py
├── owner.py
├── customer.py
├── database.py
└── store.db
```

---

# How to Run the Project

1. Clone the repository

```
git clone https://github.com/yourusername/store-management-system.git
```

2. Navigate to the project folder

```
cd store-management-system
```

3. Run the program

```
python main.py
```

---

# Example Bill

```
================================
        PRATITI MART
================================
Date: 09-03-2026
--------------------------------
Product: Milk
Price: 30
Quantity: 2
--------------------------------
TOTAL: 60
================================
Thank you for shopping!
================================
```

---

# Future Improvements

* Cart system for multiple products
* Sales reports and analytics
* Low stock alerts
* Receipt file generation
* GUI version using Tkinter

---

# Author

Developed as a Python and SQLite project to demonstrate inventory management, billing logic, and database integration for a simple store system.
