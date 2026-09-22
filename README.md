FastAPI Authentication and RBAC Service
A production-ready backend authentication system designed with FastAPI, SQLAlchemy, and SQLite. This project demonstrates a secure, scalable approach to user management, implementing stateless JWT authentication and strict Role-Based Access Control (RBAC) to separate standard users from administrators.

Key Architecture and Security Features
JWT Session Management: Secure, stateless API interactions using JSON Web Tokens (Bearer type).

Role-Based Access Control (RBAC): Dedicated dependency injection to strictly enforce endpoint authorization based on user roles (user vs. admin).

Cryptographic Security: Passwords are never stored in plain text. The system utilizes bcrypt via the passlib library for advanced cryptographic hashing.

Data Validation: Comprehensive schema enforcement and payload validation using Pydantic.

ORM Database Operations: Clean, object-oriented database interactions using SQLAlchemy mapped to a local SQLite instance.

Interactive API Documentation: Auto-generated OpenAPI integration (Swagger UI) for seamless endpoint testing.

Tech Stack
Framework: FastAPI

Server: Uvicorn

Database: SQLite and SQLAlchemy (ORM)

Authentication: Python-jose (JWT), OAuth2 with Password (and hashing), Passlib

Data Models: Pydantic

API Endpoints
POST /signup - Public - Registers a new user and hashes the password. Default role: user.

POST /login - Public - Authenticates credentials and returns a JWT Bearer token.

GET /users/me - Protected - Returns the profile data of the currently authenticated user.

GET /users/admin - Admin Only - Returns a list of all registered users. Blocked with HTTP 403 for non-admins.

Local Setup and Installation
Clone the repository:
git clone https://github.com/yotamilany1-star/auth_project.git
cd auth_project

Initialize a virtual environment:
python -m venv .venv
.venv\Scripts\activate

Install dependencies:
pip install fastapi uvicorn sqlalchemy pydantic passlib bcrypt python-jose email-validator python-multipart

Launch the server:
uvicorn main:app --reload

Navigate to http://127.0.0.1:8000/docs to explore the interactive API documentation.

Initializing the First Administrator (Super User)
To maintain strict security, the /signup endpoint intentionally assigns the standard user role to all new accounts. The system does not allow client-side role assignment. To test admin-protected routes, the first administrator must be promoted manually at the database level:

Launch the server and navigate to the Swagger UI (/docs).

Register a new user via the POST /signup endpoint.

Open the generated app.db (or sql_app.db) file using an SQLite database viewer.

Locate the users table, find your newly created user record, and change the value in the role column from "user" to "admin".

Write and commit the changes to the database file.

Re-authenticate via POST /login to generate a new JWT token containing your updated administrative privileges. You can now successfully access GET /users/admin.
