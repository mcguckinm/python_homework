import sqlite3
import os

os.chdir(os.path.dirname(__file__))

#print("CWD:",os.getcwd())
#print("DB exists:", os.path.isfile("../db/lesson.db"))


def average_order_price_per_customer(cursor):
    query = """
            SELECT
                customers.customer_name,
                AVG(sub.total_price) AS average_total_price
            FROM customers
            LEFT JOIN (
                SELECT
                    orders.customer_id AS customer_id_b,
                    SUM(line_items.quantity * products.price) AS total_price
                FROM orders
                JOIN line_items ON orders.order_id = line_items.order_id
                JOIN products ON line_items.product_id = products.product_id
                GROUP BY orders.order_id
            ) AS sub
            ON customers.customer_id = sub.customer_id_b
            GROUP BY customers.customer_id
            ORDER BY customers.customer_name;
            """
    cursor.execute(query)
    rows = cursor.fetchall()
    print("\nAverage Order Price Per Customer:")
    for name, avg_price in rows:
        if avg_price is None:
            print(f"{name}: No Orders")
        else:
            print(f"{name}: ${avg_price:.2f}")

def employees_with_more_than_5_orders(cursor):
    query = """
            SELECT
                employees.employee_id,
                employees.first_name,
                employees.last_name,
                COUNT(orders.order_id) AS order_count
            FROM employees
            JOIN orders
                ON employees.employee_id = orders.employee_id
            GROUP BY
                employees.employee_id,
                employees.first_name,
                employees.last_name
            HAVING COUNT(orders.order_id) > 5
            ORDER BY order_count DESC;
            """
    cursor.execute(query)
    rows = cursor.fetchall()

    print("\nTask 4")
    for employee_id, first_name, last_name, order_count in rows:
        print(f"{employee_id}: {first_name} {last_name} - {order_count} orders")

def main():
    conn = sqlite3.connect("../db/lesson.db")
    cursor = conn.cursor()
    #cursor.execute("PRAGMA table_info(customers);")
    conn.execute("PRAGMA foreign_keys = 1")
    #print(cursor.fetchall())
    try:

        cursor.execute("""
                   SELECT customer_id
                   FROM customers
                   WHERE customer_name = ?
                   """,("Perez and Sons",))
        row = cursor.fetchone()
        if row is None:
            raise ValueError("Customer 'Perez and Sons' not found.")
        customer_id = row[0]
    
        cursor.execute("""
                   SELECT employee_id
                   FROM employees
                   WHERE first_name = ? AND last_name = ?
                   """,("Miranda", "Harris"))
        row = cursor.fetchone()
        if row is None:
            raise ValueError("Employee 'Miranda Harris' not found.")
        employee_id = row[0]
    
        cursor.execute("""
                   SELECT product_id
                   FROM products
                   ORDER BY price ASC
                   LIMIT 5
                   """)
        product_ids = [r[0] for r in cursor.fetchall()]
        if len(product_ids) != 5:
            raise ValueError("Could not retrieve 5 cheapest products.")
        

        cursor.execute("""
                   INSERT INTO orders (customer_id, employee_id)
                   VALUES (?,?)
                   RETURNING order_id
                   """,(customer_id, employee_id))
        order_id = cursor.fetchone()[0]
    
        for pid in product_ids:
            cursor.execute("""
                           INSERT INTO line_items (order_id, product_id, quantity)
                           VALUES (?, ?, ?)
                           """, (order_id, pid, 10))

        conn.commit()
        cursor.execute("""
            SELECT
                line_items.line_item_id,
                line_items.quantity,
                products.product_name
            FROM line_items
            JOIN products ON line_items.product_id = products.product_id
            WHERE line_items.order_id = ?
            ORDER BY line_items.line_item_id
        """, (order_id,))
        new_items = cursor.fetchall()

        print(f"\nTask 3 - New order created (order_id={order_id}). Line items:")
        for line_item_id, qty, product_name in new_items:
            print(f"{line_item_id}: {qty} x {product_name}")

    except Exception as e:
        conn.rollback()
        print("Task 3 failed, rolled back transaction:", e)

    query = """SELECT 
                orders.order_id,
                SUM(line_items.quantity * products.price) AS total_price
                FROM orders
                JOIN line_items ON orders.order_id = line_items.order_id
                JOIN products ON line_items.product_id = products.product_id
                GROUP BY orders.order_id
                ORDER BY orders.order_id
                LIMIT 5;
                """
    cursor.execute(query)
    rows = cursor.fetchall()

    print("\nFirst 5 Orders - Total Prices")
    for order_id, total_price in rows:
        print(f"order {order_id}: ${total_price:.2f}")
    average_order_price_per_customer(cursor)
    

    
    
    employees_with_more_than_5_orders(cursor)

    conn.close()


if __name__ == "__main__":
    main()

