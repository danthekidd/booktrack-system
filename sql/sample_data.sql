PRAGMA foreign_keys = ON;

INSERT INTO customers (first_name, last_name, email, phone) VALUES
('Ava', 'Miller', 'ava.miller@email.com', '555-0101'),
('Noah', 'Johnson', 'noah.johnson@email.com', '555-0102'),
('Liam', 'Brown', 'liam.brown@email.com', '555-0103'),
('Emma', 'Davis', 'emma.davis@email.com', '555-0104'),
('Sophia', 'Wilson', 'sophia.wilson@email.com', '555-0105');

INSERT INTO employees (first_name, last_name, role, email, hire_date) VALUES
('Mia', 'Clark', 'Cashier', 'mia.clark@booktrack.com', '2024-02-15'),
('Ethan', 'Hall', 'Manager', 'ethan.hall@booktrack.com', '2023-10-01'),
('Olivia', 'Young', 'Sales Associate', 'olivia.young@booktrack.com', '2025-01-10');

INSERT INTO publishers (publisher_name, city, country) VALUES
('Penguin Random House', 'New York', 'USA'),
('HarperCollins', 'New York', 'USA'),
('Simon & Schuster', 'New York', 'USA'),
('Macmillan Publishers', 'London', 'UK');

INSERT INTO books (title, isbn, publisher_id, publication_year, genre, price, stock_quantity) VALUES
('The Silent Patient', '9781250301697', 1, 2019, 'Thriller', 14.99, 25),
('Atomic Habits', '9780735211292', 2, 2018, 'Self-Help', 18.50, 30),
('Educated', '9780399590504', 1, 2018, 'Memoir', 16.75, 18),
('Where the Crawdads Sing', '9780735219090', 3, 2018, 'Fiction', 15.99, 22),
('Project Hail Mary', '9780593135204', 4, 2021, 'Science Fiction', 21.00, 15),
('Deep Work', '9781455586691', 2, 2016, 'Productivity', 17.25, 20);

INSERT INTO orders (customer_id, employee_id, order_date, status) VALUES
(1, 1, '2026-04-01 11:15:00', 'Completed'),
(2, 1, '2026-04-03 14:25:00', 'Completed'),
(3, 3, '2026-04-06 16:05:00', 'Pending'),
(1, 3, '2026-04-08 10:45:00', 'Completed'),
(5, 2, '2026-04-10 12:10:00', 'Completed');

INSERT INTO order_items (order_id, book_id, quantity, unit_price) VALUES
(1, 1, 1, 14.99),
(1, 2, 1, 18.50),
(2, 4, 2, 15.99),
(3, 5, 1, 21.00),
(4, 3, 1, 16.75),
(4, 6, 1, 17.25),
(5, 2, 2, 18.50),
(5, 1, 1, 14.99);
