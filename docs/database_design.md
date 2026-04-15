# Database Design (3NF): Bookstore Inventory and Order Management System

## Tables and Keys

### 1) customers
- `customer_id` (PK)
- `first_name`
- `last_name`
- `email` (UNIQUE)
- `phone`
- `created_at`

### 2) employees
- `employee_id` (PK)
- `first_name`
- `last_name`
- `role`
- `email` (UNIQUE)
- `hire_date`

### 3) publishers
- `publisher_id` (PK)
- `publisher_name` (UNIQUE)
- `city`
- `country`

### 4) books
- `book_id` (PK)
- `title`
- `isbn` (UNIQUE)
- `publisher_id` (FK -> publishers.publisher_id)
- `publication_year`
- `genre`
- `price`
- `stock_quantity`

### 5) orders
- `order_id` (PK)
- `customer_id` (FK -> customers.customer_id)
- `employee_id` (FK -> employees.employee_id)
- `order_date`
- `status`

### 6) order_items
- `order_item_id` (PK)
- `order_id` (FK -> orders.order_id)
- `book_id` (FK -> books.book_id)
- `quantity`
- `unit_price`
- `UNIQUE(order_id, book_id)` to prevent duplicate same-book lines in one order

## Relationship Summary
- `publishers` 1:M `books`
- `customers` 1:M `orders`
- `employees` 1:M `orders`
- `orders` M:N `books` resolved by `order_items`

## Why the Design is in 1NF, 2NF, and 3NF

### 1NF (First Normal Form)
- All tables have primary keys.
- Every column is atomic (no repeating groups or multi-valued fields).
- Each row stores one record of one entity.

### 2NF (Second Normal Form)
- The schema is already in 1NF.
- Non-key attributes depend on the full primary key.
- In `order_items`, line details (`quantity`, `unit_price`) depend on the order-book line, not partially on unrelated attributes.

### 3NF (Third Normal Form)
- The schema is in 2NF.
- Non-key fields do not depend on other non-key fields (no transitive dependency).
  - Example: publisher details are stored in `publishers`, not duplicated in `books`.
  - Customer and employee details are stored in their own tables, not inside `orders`.
- This reduces redundancy and update anomalies.
