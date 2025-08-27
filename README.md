Grocery Store Management Application 🛒


This project is a 3-tier Grocery Store Management Application designed to simplify grocery ordering, product management, and order tracking.

1.Frontend: Built using HTML, CSS, JavaScript, and Bootstrap for a clean and responsive user interface.
2.Backend: Developed using Python Flask Framework to handle APIs, server logic, and communication with the database.
3.Database: MySQL is used to store product details, orders, and unit-of-measure information.


📂 Project Structure

Grocery application/
│── backend/
│   ├── orders_dao.py
│   ├── products_dao.py
│   ├── server.py
│   ├── sql_connection.py
│   └── uom_dao.py
│
│── gs-application/
│   └── User interface/
│       ├── ui/
│       │   ├── css/
│       │   ├── images/
│       │   └── js/
│       ├── index.html
│       ├── manage-product.html
│       └── order.html
│
└── README.md


⚙ Workflow

1. Frontend (User Interface)

Customers/Users interact via responsive HTML pages styled with CSS/Bootstrap and powered by JavaScript.
Pages include:
index.html → Homepage
manage-product.html → Manage grocery products
order.html → Place and track orders


2. Backend (Flask)

server.py runs a Flask app exposing REST APIs.
Data access logic is divided into DAO (Data Access Objects):
orders_dao.py → Order operations
products_dao.py → Product operations
uom_dao.py → Unit of Measure operations
sql_connection.py handles database connection.

3. Database (MySQL)

Stores:
Product details
Order details
Unit of Measure (UOM)


**How to Run the Project
**
🔧 Prerequisites

Python
Flask
MySQL Server
Web browser

▶ Steps

1. Clone the Repository

git clone <your-repo-url>
cd Grocery-application


2. Set Up Database

Install MySQL and create a database (e.g., grocery_db).
Update connection details in sql_connection.py.
Import your schema & tables (if you have .sql file, run it in MySQL).



3. Install Dependencies

pip install flask mysql-connector-python

4. Run the Flask Server

cd backend
python server.py


✨ Features

Add, update, delete grocery products
Place and manage orders
User-friendly interface with Bootstrap
Persistent data storage using MySQL
REST API-based backend

---
