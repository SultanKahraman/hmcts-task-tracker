HMCTS Caseworker Task Tracker

This repository contains the solution for the DTS Developer Technical Test. The objective was to develop a simple system for caseworkers to create and track tasks, focusing on best coding practices, validation, and documentation.

---------------------------------------------------------------------------------------------------------

📦 Technology Stack

Backend: Python 3, Flask, Flask-SQLAlchemy, Flask-CORS

Database: SQLite

Frontend: HTML, CSS, Vanilla JavaScript (ES6+)

---------------------------------------------------------------------------------------------------------
Prerequisites for checking the task

You need to have Python 3 and pip installed on your system.

1. Clone the Repository

git clone [YOUR-REPOSITORY-URL]
cd [YOUR-REPOSITORY-NAME]

2. Set up the Backend

Navigate into the backend directory and install the required Python packages.

cd backend
pip install Flask Flask-SQLAlchemy Flask-CORS
cd .. # Return to the root directory

---------------------------------------------------------------------------------------------------------

🚀 Running the Application

The application requires two separate processes to run concurrently: the Backend API (Python) and the Frontend UI (a simple HTTP server).

1. Start the Backend API

This process will also initialize the tasks.db SQLite file if it doesn't already exist.

python3 backend/app.py


The API server will start on port 5000 (e.g., http://127.0.0.1:5000/). Keep this terminal window open.

2. Start the Frontend UI

Open a new terminal window, navigate into the frontend directory, and start a simple local HTTP server.

cd frontend
python3 -m http.server 8000


The frontend UI will be available at http://localhost:8000.

---------------------------------------------------------------------------------------------------------

🖥️ Usage

Open your browser to http://localhost:8000.

Fill in the Title and Due Date/Time (both required).

Click "Create Task".

The form sends a POST request to the backend. On successful creation, a confirmation message and the details of the newly created task are displayed.

---------------------------------------------------------------------------------------------------------
