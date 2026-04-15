# BookTrack System (Python + SQLite)

A beginner-friendly **Bookstore Inventory and Order Management System** built for a college database project rubric.

## Complete Folder Structure
```text
booktrack-system/
├── README.md
├── main.py
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

## File-by-File Overview
- `main.py`: terminal menu for setup, CRUD, order creation, and reporting.
- `src/db.py`: SQLite connection helper with foreign keys enabled.
- `src/setup_db.py`: creates tables and inserts sample data from SQL files.
- `src/crud.py`: customer, book, and order operations with error handling.
- `src/queries.py`: required simple, join, aggregation, and subquery reports.
- `sql/schema.sql`: complete table creation script with PK/FK constraints.
- `sql/sample_data.sql`: realistic starter data for all entities.
- `docs/project_proposal.md`: proposal section required by rubric.
- `docs/database_design.md`: normalized design and 1NF/2NF/3NF explanation.
- `docs/word_ready_documentation.md`: Word-document-ready write-up.

## How to Run
1. Ensure Python 3 is installed.
2. Open terminal in the project folder.
3. Run:
   ```bash
   python main.py
   ```
4. In the menu:
   - `1` create tables
   - `2` insert sample data
   - `13` run required queries
