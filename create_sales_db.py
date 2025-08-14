import sqlite3

# Create a new DB file
conn = sqlite3.connect("sales_data.db")
cur = conn.cursor()

# Create the sales table
cur.execute("""
CREATE TABLE sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_date TEXT NOT NULL,
    product TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    price REAL NOT NULL
)
""")

conn.commit()
conn.close()


import sqlite3

data = [
    ("2025-08-01", "Wireless Mouse", 3, 14.99),
    ("2025-08-01", "USB-C Cable", 5, 6.50),
    ("2025-08-02", "Headphones", 2, 39.00),
    ("2025-08-02", "Laptop Sleeve", 1, 18.00),
    ("2025-08-03", "Webcam", 1, 49.99),
]

conn = sqlite3.connect("sales_data.db")
cur = conn.cursor()

cur.executemany("""
INSERT INTO sales (order_date, product, quantity, price)
VALUES (?, ?, ?, ?)
""", data)

conn.commit()
conn.close()
