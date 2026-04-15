"""Simple terminal menu for the Bookstore Inventory and Order Management System."""

from src.crud import (
    add_book,
    add_customer,
    create_order,
    delete_book,
    delete_customer,
    update_book_stock_price,
    update_customer,
    view_books,
    view_customers,
    view_orders,
)
from src.queries import run_all_required_queries
from src.setup_db import create_tables, insert_sample_data


def print_menu():
    print("\n=== BookTrack System Menu ===")
    print("1. Create tables")
    print("2. Insert sample data")
    print("3. Add customer")
    print("4. View customers")
    print("5. Update customer")
    print("6. Delete customer")
    print("7. Add book")
    print("8. View books")
    print("9. Update book stock/price")
    print("10. Delete book")
    print("11. Create order")
    print("12. View orders")
    print("13. Run required queries")
    print("0. Exit")


def handle_add_customer():
    first_name = input("First name: ").strip()
    last_name = input("Last name: ").strip()
    email = input("Email: ").strip()
    phone = input("Phone: ").strip()
    add_customer(first_name, last_name, email, phone)


def handle_update_customer():
    customer_id = int(input("Customer ID to update: ").strip())
    new_email = input("New email: ").strip()
    new_phone = input("New phone: ").strip()
    update_customer(customer_id, new_email, new_phone)


def handle_delete_customer():
    customer_id = int(input("Customer ID to delete: ").strip())
    delete_customer(customer_id)


def handle_add_book():
    title = input("Title: ").strip()
    isbn = input("ISBN: ").strip()
    publisher_id = int(input("Publisher ID: ").strip())
    publication_year = int(input("Publication year: ").strip())
    genre = input("Genre: ").strip()
    price = float(input("Price: ").strip())
    stock_quantity = int(input("Stock quantity: ").strip())
    add_book(title, isbn, publisher_id, publication_year, genre, price, stock_quantity)


def handle_update_book():
    book_id = int(input("Book ID to update: ").strip())
    new_stock = int(input("New stock quantity: ").strip())
    new_price = float(input("New price: ").strip())
    update_book_stock_price(book_id, new_stock, new_price)


def handle_delete_book():
    book_id = int(input("Book ID to delete: ").strip())
    delete_book(book_id)


def handle_create_order():
    customer_id = int(input("Customer ID: ").strip())
    employee_id = int(input("Employee ID: ").strip())

    items = []
    print("Enter book items for this order.")
    print("Type 0 for Book ID when finished.")

    while True:
        book_id = int(input("Book ID: ").strip())
        if book_id == 0:
            break

        quantity = int(input("Quantity: ").strip())
        items.append((book_id, quantity))

    if not items:
        print("No items entered. Order canceled.")
        return

    create_order(customer_id, employee_id, items)


def main():
    while True:
        try:
            print_menu()
            choice = input("Select an option: ").strip()

            if choice == "1":
                create_tables()
            elif choice == "2":
                insert_sample_data()
            elif choice == "3":
                handle_add_customer()
            elif choice == "4":
                view_customers()
            elif choice == "5":
                handle_update_customer()
            elif choice == "6":
                handle_delete_customer()
            elif choice == "7":
                handle_add_book()
            elif choice == "8":
                view_books()
            elif choice == "9":
                handle_update_book()
            elif choice == "10":
                handle_delete_book()
            elif choice == "11":
                handle_create_order()
            elif choice == "12":
                view_orders()
            elif choice == "13":
                run_all_required_queries()
            elif choice == "0":
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please choose a valid menu number.")
        except ValueError:
            print("Input error: please enter numbers where required.")
        except Exception as error:
            print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()
