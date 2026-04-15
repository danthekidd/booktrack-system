"""CRUD operations for customers, books, and orders."""

from src.db import get_connection


# -------------------------
# Customer CRUD operations
# -------------------------
def add_customer(first_name, last_name, email, phone):
    try:
        with get_connection() as connection:
            connection.execute(
                """
                INSERT INTO customers (first_name, last_name, email, phone)
                VALUES (?, ?, ?, ?)
                """,
                (first_name, last_name, email, phone),
            )
            print("Customer added successfully.")
    except Exception as error:
        print(f"Error adding customer: {error}")


def view_customers():
    try:
        with get_connection() as connection:
            rows = connection.execute(
                "SELECT customer_id, first_name, last_name, email, phone FROM customers"
            ).fetchall()
            if not rows:
                print("No customers found.")
                return

            print("\nCustomers")
            print("-" * 70)
            for row in rows:
                print(
                    f"ID: {row['customer_id']} | "
                    f"Name: {row['first_name']} {row['last_name']} | "
                    f"Email: {row['email']} | Phone: {row['phone']}"
                )
    except Exception as error:
        print(f"Error viewing customers: {error}")


def update_customer(customer_id, new_email, new_phone):
    try:
        with get_connection() as connection:
            cursor = connection.execute(
                """
                UPDATE customers
                SET email = ?, phone = ?
                WHERE customer_id = ?
                """,
                (new_email, new_phone, customer_id),
            )
            if cursor.rowcount == 0:
                print("Customer not found.")
            else:
                print("Customer updated successfully.")
    except Exception as error:
        print(f"Error updating customer: {error}")


def delete_customer(customer_id):
    try:
        with get_connection() as connection:
            cursor = connection.execute(
                "DELETE FROM customers WHERE customer_id = ?", (customer_id,)
            )
            if cursor.rowcount == 0:
                print("Customer not found.")
            else:
                print("Customer deleted successfully.")
    except Exception as error:
        print(f"Error deleting customer: {error}")


# -------------------------
# Book CRUD operations
# -------------------------
def add_book(title, isbn, publisher_id, publication_year, genre, price, stock_quantity):
    try:
        with get_connection() as connection:
            connection.execute(
                """
                INSERT INTO books
                    (title, isbn, publisher_id, publication_year, genre, price, stock_quantity)
                VALUES
                    (?, ?, ?, ?, ?, ?, ?)
                """,
                (title, isbn, publisher_id, publication_year, genre, price, stock_quantity),
            )
            print("Book added successfully.")
    except Exception as error:
        print(f"Error adding book: {error}")


def view_books():
    try:
        with get_connection() as connection:
            rows = connection.execute(
                """
                SELECT b.book_id, b.title, b.price, b.stock_quantity, p.publisher_name
                FROM books b
                JOIN publishers p ON b.publisher_id = p.publisher_id
                ORDER BY b.book_id
                """
            ).fetchall()
            if not rows:
                print("No books found.")
                return

            print("\nBooks")
            print("-" * 90)
            for row in rows:
                print(
                    f"ID: {row['book_id']} | Title: {row['title']} | "
                    f"Publisher: {row['publisher_name']} | "
                    f"Price: ${row['price']:.2f} | Stock: {row['stock_quantity']}"
                )
    except Exception as error:
        print(f"Error viewing books: {error}")


def update_book_stock_price(book_id, new_stock, new_price):
    try:
        with get_connection() as connection:
            cursor = connection.execute(
                """
                UPDATE books
                SET stock_quantity = ?, price = ?
                WHERE book_id = ?
                """,
                (new_stock, new_price, book_id),
            )
            if cursor.rowcount == 0:
                print("Book not found.")
            else:
                print("Book updated successfully.")
    except Exception as error:
        print(f"Error updating book: {error}")


def delete_book(book_id):
    try:
        with get_connection() as connection:
            cursor = connection.execute("DELETE FROM books WHERE book_id = ?", (book_id,))
            if cursor.rowcount == 0:
                print("Book not found.")
            else:
                print("Book deleted successfully.")
    except Exception as error:
        print(f"Error deleting book: {error}")


# -------------------------
# Order operations
# -------------------------
def create_order(customer_id, employee_id, items):
    """
    Create a new order.

    items is a list of tuples in this format:
    [(book_id, quantity), (book_id, quantity), ...]
    """
    try:
        with get_connection() as connection:
            cursor = connection.execute(
                "INSERT INTO orders (customer_id, employee_id, status) VALUES (?, ?, 'Completed')",
                (customer_id, employee_id),
            )
            order_id = cursor.lastrowid

            for book_id, quantity in items:
                book = connection.execute(
                    "SELECT price, stock_quantity FROM books WHERE book_id = ?", (book_id,)
                ).fetchone()

                if not book:
                    raise ValueError(f"Book with ID {book_id} does not exist.")

                if quantity > book["stock_quantity"]:
                    raise ValueError(
                        f"Not enough stock for book ID {book_id}. "
                        f"Available: {book['stock_quantity']}"
                    )

                unit_price = book["price"]
                connection.execute(
                    """
                    INSERT INTO order_items (order_id, book_id, quantity, unit_price)
                    VALUES (?, ?, ?, ?)
                    """,
                    (order_id, book_id, quantity, unit_price),
                )

                connection.execute(
                    """
                    UPDATE books
                    SET stock_quantity = stock_quantity - ?
                    WHERE book_id = ?
                    """,
                    (quantity, book_id),
                )

            print(f"Order {order_id} created successfully.")
    except Exception as error:
        print(f"Error creating order: {error}")


def view_orders():
    try:
        with get_connection() as connection:
            rows = connection.execute(
                """
                SELECT
                    o.order_id,
                    o.order_date,
                    c.first_name || ' ' || c.last_name AS customer_name,
                    e.first_name || ' ' || e.last_name AS employee_name,
                    o.status,
                    ROUND(SUM(oi.quantity * oi.unit_price), 2) AS order_total
                FROM orders o
                JOIN customers c ON o.customer_id = c.customer_id
                JOIN employees e ON o.employee_id = e.employee_id
                JOIN order_items oi ON o.order_id = oi.order_id
                GROUP BY o.order_id, o.order_date, customer_name, employee_name, o.status
                ORDER BY o.order_id
                """
            ).fetchall()

            if not rows:
                print("No orders found.")
                return

            print("\nOrders")
            print("-" * 110)
            for row in rows:
                print(
                    f"Order ID: {row['order_id']} | Date: {row['order_date']} | "
                    f"Customer: {row['customer_name']} | Employee: {row['employee_name']} | "
                    f"Status: {row['status']} | Total: ${row['order_total']:.2f}"
                )
    except Exception as error:
        print(f"Error viewing orders: {error}")
