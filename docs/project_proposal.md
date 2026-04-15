# Project Proposal: Bookstore Inventory and Order Management System

## 1) Project Idea
This project is a beginner-friendly database application for a bookstore. It tracks books, publishers, customers, employees, orders, and items in each order. The system uses Python and SQLite with a terminal menu for day-to-day operations.

## 2) Purpose
The purpose is to demonstrate how to design and implement a relational database system that supports:
- Inventory tracking (books, stock, prices)
- Customer and employee record management
- Order creation and order-history reporting
- SQL query skills (simple, joins, aggregation, subqueries)

## 3) Key Entities
- **customers**: people who buy books
- **employees**: staff who process customer orders
- **publishers**: companies that publish books
- **books**: catalog of products sold by the bookstore
- **orders**: one transaction per customer purchase
- **order_items**: line-by-line items inside each order (junction table)

## 4) Relationships
- One publisher can publish many books (`publishers` 1-to-many `books`).
- One customer can place many orders (`customers` 1-to-many `orders`).
- One employee can manage many orders (`employees` 1-to-many `orders`).
- One order can contain many books and one book can appear in many orders.
  - This many-to-many relationship is resolved by `order_items`.

## 5) Expected Features
- Create database and tables
- Insert sample data for testing
- CRUD for customers
- CRUD for books
- Create and view orders
- Basic stock deduction when orders are created
- Error handling with `try/except`
- Reporting queries from the rubric

## 6) Expected Queries
- List all books with publisher names (join)
- Show all orders with customer names (join)
- Total sales by customer (aggregation)
- Total quantity sold per book (aggregation)
- Most expensive book (subquery)
- Customers who spent more than average (subquery + aggregation)
