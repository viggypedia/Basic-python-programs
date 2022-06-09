import sqlite3

#By: S Vignesh Nelakantan
#Reg.No: RA2011003010530

# Connect to database
connection = sqlite3.connect('q3.db')

# Create cursor
cursor = connection.cursor()

# Create table
# orders table
cursor.execute("""CREATE TABLE orders (
    order_id integer PRIMARY KEY,
    product_id integer,
    unit_price integer,
    quantity integer
)""")

# # insert data
orders = [
    (101, 1, 450, 2), 
    (102, 2, 500, 3)
]

cursor.executemany("INSERT INTO orders VALUES (?, ?, ?, ?)", orders)

# products table
cursor.execute("""CREATE TABLE products (
    product_id integer PRIMARY KEY,
    product_name text,
    unit_price integer,
    supplier_id integer,
    package integer,
    order_id integer,
    FOREIGN KEY (order_id) REFERENCES orders (order_id)
)""")

# insert data
products = [
    (1, "material ui", 450, 1, 5, 101),
    (2, "tailwind css", 500, 2, 6, 102)
]

cursor.executemany("INSERT INTO products VALUES (?, ?, ?, ?, ?, ?)", products)

# query to db
cursor.execute("SELECT * FROM orders")
orders = cursor.fetchall()
cursor.execute("SELECT * FROM products")
products = cursor.fetchall()
print(orders)
print('-----------------------------------------------------')
print(products)
print("-----------------------------------------------------")

cursor.execute("SELECT product.package-orde.quantity FROM products product, orders orde WHERE product.order_id = orde.order_id")
products = cursor.fetchall()
print(products)
print("-----------------------------------------------------")

cursor.execute("SELECT unit_price FROM products ORDER BY supplier_id DESC")
products = cursor.fetchall()
print(products)
print('-----------------------------------------------------')

cursor.execute("SELECT product_name, supplier_id, order_id FROM products")
products = cursor.fetchall()
print(products)

# Commit changes
connection.commit()

# Close connection
connection.close()

