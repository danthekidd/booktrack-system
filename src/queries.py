"""Reporting queries: retrieval, joins, aggregation, and subqueries."""

from src.db import get_connection


def run_and_print_query(title, sql_query, params=()):
    """Helper function to run a query and print results in a clean format."""
    try:
        with get_connection() as connection:
            rows = connection.execute(sql_query, params).fetchall()
            print(f"\n{title}")
            print("-" * len(title))

            if not rows:
                print("No data returned.")
                return

            headers = rows[0].keys()
            print(" | ".join(headers))
            print("-" * 100)
            for row in rows:
                print(" | ".join(str(row[column]) for column in headers))
    except Exception as error:
        print(f"Error running query '{title}': {error}")


def list_books_with_publishers():
    query = """
    SELECT b.book_id, b.title, p.publisher_name, b.price, b.stock_quantity
    FROM books b
    JOIN publishers p ON b.publisher_id = p.publisher_id
    ORDER BY b.title
    """
    run_and_print_query("Books with Publisher Names", query)


def show_orders_with_customer_names():
    query = """
    SELECT
        o.order_id,
        c.first_name || ' ' || c.last_name AS customer_name,
        o.order_date,
        o.status
    FROM orders o
    JOIN customers c ON o.customer_id = c.customer_id
    ORDER BY o.order_date DESC
    """
    run_and_print_query("Orders with Customer Names", query)


def total_sales_by_customer():
    query = """
    SELECT
        c.customer_id,
        c.first_name || ' ' || c.last_name AS customer_name,
        ROUND(SUM(oi.quantity * oi.unit_price), 2) AS total_spent
    FROM customers c
    JOIN orders o ON c.customer_id = o.customer_id
    JOIN order_items oi ON o.order_id = oi.order_id
    GROUP BY c.customer_id, customer_name
    ORDER BY total_spent DESC
    """
    run_and_print_query("Total Sales by Customer", query)


def total_quantity_sold_per_book():
    query = """
    SELECT
        b.book_id,
        b.title,
        SUM(oi.quantity) AS total_quantity_sold
    FROM books b
    JOIN order_items oi ON b.book_id = oi.book_id
    GROUP BY b.book_id, b.title
    ORDER BY total_quantity_sold DESC, b.title
    """
    run_and_print_query("Total Quantity Sold per Book", query)


def most_expensive_book():
    query = """
    SELECT book_id, title, price
    FROM books
    WHERE price = (SELECT MAX(price) FROM books)
    """
    run_and_print_query("Most Expensive Book", query)


def customers_above_average_spending():
    query = """
    SELECT customer_name, total_spent
    FROM (
        SELECT
            c.customer_id,
            c.first_name || ' ' || c.last_name AS customer_name,
            ROUND(SUM(oi.quantity * oi.unit_price), 2) AS total_spent
        FROM customers c
        JOIN orders o ON c.customer_id = o.customer_id
        JOIN order_items oi ON o.order_id = oi.order_id
        GROUP BY c.customer_id, customer_name
    ) customer_totals
    WHERE total_spent > (
        SELECT AVG(total_per_customer)
        FROM (
            SELECT SUM(oi2.quantity * oi2.unit_price) AS total_per_customer
            FROM orders o2
            JOIN order_items oi2 ON o2.order_id = oi2.order_id
            GROUP BY o2.customer_id
        ) avg_source
    )
    ORDER BY total_spent DESC
    """
    run_and_print_query("Customers Spending Above Average", query)


def run_all_required_queries():
    """Run all required rubric queries in sequence."""
    list_books_with_publishers()
    show_orders_with_customer_names()
    total_sales_by_customer()
    total_quantity_sold_per_book()
    most_expensive_book()
    customers_above_average_spending()
