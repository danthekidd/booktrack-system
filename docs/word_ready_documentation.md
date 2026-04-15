# Bookstore Inventory and Order Management System

## Project Description
This project is a console-based database system developed using Python and SQLite. It is designed for a bookstore that needs to manage inventory, customer records, staff activity, and sales orders. The project demonstrates core relational database concepts and practical database programming.

## Technology Stack
- Programming Language: Python 3
- Database: SQLite
- Interface: Text-based terminal menu

## Folder Structure
```text
booktrack-system/
├── main.py
├── booktrack.db                    # created at runtime
├── src/
│   ├── __init__.py
│   ├── db.py
│   ├── setup_db.py
│   ├── crud.py
│   └── queries.py
├── sql/
│   ├── schema.sql
│   └── sample_data.sql
└── docs/
    ├── project_proposal.md
    ├── database_design.md
    └── word_ready_documentation.md
```

## Setup Instructions
1. Open a terminal in the project directory.
2. Run the application:
   ```bash
   python main.py
   ```
3. From the menu:
   - Choose **1** to create tables.
   - Choose **2** to insert sample data.
   - Use other menu options for CRUD operations and reports.

## Database Structure
The system contains six tables:
- `customers`
- `employees`
- `publishers`
- `books`
- `orders`
- `order_items`

### Key Relationship Notes
- One publisher can have many books.
- One customer can place many orders.
- One employee can process many orders.
- One order can include many books, and one book can appear in many orders.
- The many-to-many relationship between orders and books is resolved through `order_items`.

## Core Functionality
- Create schema from SQL file
- Load realistic sample data
- Customer CRUD operations
- Book CRUD operations
- Order creation with stock validation and deduction
- Order viewing with total calculation
- Query reports with joins, aggregation, and subqueries

## Sample Queries Included
1. List all books with publisher names.
2. Show all orders with customer names.
3. Total sales by customer.
4. Total quantity sold per book.
5. Most expensive book.
6. Customers who spent more than the average customer.

## Example Results (after loading sample data)
- You can view a merged list of books and their publishers.
- You can view each order with customer and employee names.
- You can identify top-spending customers and top-selling books.
- You can identify premium/highest-price titles.

## Error Handling and Coding Practices
- All database operations are wrapped in `try/except` blocks.
- SQL uses parameterized placeholders (`?`) to avoid string interpolation mistakes.
- Functions are split by responsibility for readability and maintainability.
- Variable names are descriptive and beginner-friendly.

## How to Run for Demonstration
1. Start app with `python main.py`.
2. Press `1` then `2`.
3. Press `4`, `8`, and `12` to verify customer, book, and order data.
4. Press `13` to run all required rubric queries.
5. Press `0` to exit.
