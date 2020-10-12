<!-- # Books-catalogue
This project records the Books read by the users. Allows to save a book, delete a book and view the books using RESTApi.
customerapi implements registration of customers and authentication.
bookapi lists the books added by the user, and allows to update and delete the books.

Steps to use the code:
----------------------
1. Clone the repository. 
2. If you prefer working in virtual environment create your virtual env using Virtualenv env_name
3. Activate the Virtual env: source env_folder/Scripts/activate
4. Install the dependencies: pip install -r requirements.txt
5. This project uses postgres, download and install postgres from https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
6. Setup PostgreSQL 
7. Apply the migrations: Python manage.py migrate
8. Run the server: python manage.py runserver
------------------------------------------------

How to use the APIs:
--------------------
1. http://127.0.0.1:8000/books/v1/
2. http://127.0.0.1:8000/books/v1/books/ --- List the books saved by the user. GET, POST, HEAD, OPTIONS. Also has DateRange Filter to query books added today, yesterday, last 7 days, this month, this year
3. http://127.0.0.1:8000/books/v1/books/?date_added=today --- query to list books added today
4. http://127.0.0.1:8000/books/v1/books/1/ --- GET, PUT, PATCH, DELETE, HEAD, OPTIONS
5. http://127.0.0.1:8000/customers/v1/
6. http://127.0.0.1:8000/customers/v1/customers/ --- List the customers. GET, POST, HEAD, OPTIONS.
7. http://127.0.0.1:8000/customers/v1/customers/1/ --- GET, PUT, PATCH, DELETE, HEAD, OPTIONS
8. http://127.0.0.1:8000/customers/v1/rest-auth/login/ --- returns token if customer is authenticated.
9. http://127.0.0.1:8000/customers/v1/rest-auth/registration/ --- new customer registration.
-------------------- -->



