Election Management System
Project Overview

The Election Management System is a backend-driven application designed to manage the complete election lifecycle in a structured and secure manner.
It focuses on voter registration, eligibility validation, and election data management, following clean architecture and modular design principles.

This project is built as a scalable backend foundation that can later be extended with:

Authentication & authorization

Admin dashboards

AI-based voter analytics

Frontend (Web / Mobile)

The system is developed using modern Python backend practices and is suitable for academic projects, real-world simulations, and resume portfolios.

Tech Stack
Backend

Python 3.12

FastAPI – High-performance web framework

Uvicorn – ASGI server

SQLAlchemy – ORM for database interactions

Pydantic – Data validation and schemas

Database

SQLite (development)

Easily extendable to MySQL / PostgreSQL

Tools & Practices

Git & GitHub for version control

Virtual Environment (venv)

Modular project structure

RESTful API design

Clean code & separation of concerns

Project Structure
backend/
 ├── app/
 │   ├── main.py          # Application entry point
 │   ├── database.py      # Database configuration
 │   ├── models/          # Database models
 │   ├── routes/          # API routes
 │   ├── schemas/         # Request/response schemas
 │   └── services/        # Business logic
 └── requirements.txt     # Project dependencies
.gitignore

How to Run Locally

Follow these steps to run the project on your local machine.

1. Clone the Repository
git clone https://github.com/charan5983/Ellection_Management_system.git
cd Ellection_Management_system

2. Create a Virtual Environment
python -m venv venv


Activate it:

Windows

venv\Scripts\activate


Linux / macOS

source venv/bin/activate

3. Install Dependencies
pip install -r backend/requirements.txt

4. Run the FastAPI Server
cd backend
uvicorn app.main:app --reload

5. Access the Application

API Base URL:

http://127.0.0.1:8000


Interactive API Docs (Swagger UI):

http://127.0.0.1:8000/docs


Alternative API Docs (ReDoc):

http://127.0.0.1:8000/redoc

Key Features (Current)

Modular FastAPI backend

Database connection setup

Clean project structure

Ready for feature expansion

Future Enhancements

User authentication & role management

Voter registration & eligibility checks

Election creation & result tracking

Admin dashboard

AI-based fraud detection & analytics

Frontend integration



1️⃣ Project Status (NEW)

Add a section like:

## Project Status
- Authentication & Authorization: ✅ Completed
- Voter Registration: ✅ Completed
- Admin Approval Flow: ✅ Completed
- Voting Logic: ⏳ In Progress

2️⃣ Features Implemented (Update)

Add or update:

## Features Implemented
- User Registration (VOTER / ADMIN)
- OAuth2-based Login with JWT
- Role-Based Access Control
- Voter Profile Creation
- Admin Voter Approval

3️⃣ How to Run Locally (VERY IMPORTANT)

Add this if not present:

## How to Run Locally

1. Clone the repository
2. Create virtual environment
3. Install dependencies:
   ```bash
   pip install -r requirements.txt


Start the server:

uvicorn app.main:app --reload


Open Swagger:
http://127.0.0.1:8000/docs


---

### 4️⃣ Authentication Flow (Brief)

```md
## Authentication Flow
1. Register user
2. Login using OAuth2
3. JWT token issued
4. Protected routes require authorization

Author

Charan Teja
MCA | Python Backend & Cloud Enthusias
