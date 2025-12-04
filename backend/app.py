from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from flask_cors import CORS

# --- Initialization ---
app = Flask(__name__)
CORS(app) # Enable CORS for frontend communication

# Configure Database (SQLite file)
# The database file will be created in the current directory
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# --- Database Model ---
class Task(db.Model):
    # Primary Key
    id = db.Column(db.Integer, primary_key=True)
    
    # Required Fields
    title = db.Column(db.String(100), nullable=False)
    due_date = db.Column(db.DateTime, nullable=False)
    
    # Optional Fields
    description = db.Column(db.String(500), nullable=True)
    
    # Default Fields
    status = db.Column(db.String(20), default='PENDING', nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        """Converts the Task object to a dictionary for JSON response."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'status': self.status,
            # Format the datetime object to a string for JSON
            'due_date': self.due_date.isoformat(), 
            'created_at': self.created_at.isoformat()
        }

# --- Setup Function ---
def create_tables():
    """Initializes the database and creates the Task table."""
    db.create_all()

# =================================================================
# 🚩 API ENDPOINT (Now correctly placed before app.run)
# =================================================================

@app.route('/api/tasks', methods=['POST'])
def create_task():
    """
    Handles the creation of a new task.
    """
    data = request.get_json()

    # 1. Validation and Error Handling
    title = data.get('title')
    due_date_str = data.get('due_date')

    if not title:
        return jsonify({'error': 'Title is a required field.'}), 400
    if not due_date_str:
        return jsonify({'error': 'Due date is a required field.'}), 400

    try:
        # Attempt to parse the date string (e.g., "2025-12-31T10:00")
        due_date_dt = datetime.fromisoformat(due_date_str.replace('Z', '+00:00'))
    except ValueError:
        return jsonify({'error': 'Invalid date/time format for due_date.'}), 400

    # 2. Database Creation
    try:
        new_task = Task(
            title=title,
            description=data.get('description'),
            due_date=due_date_dt
        )
        db.session.add(new_task)
        db.session.commit()

        # 3. Successful Response
        return jsonify({
            'message': 'Task successfully created!',
            'task': new_task.to_dict()
        }), 201 # HTTP 201 Created

    except Exception as e:
        # Generic server error
        db.session.rollback()
        print(f"Database error: {e}")
        return jsonify({'error': 'An internal error occurred during task creation.'}), 500

# --- Run the App ---
if __name__ == '__main__':
    # Initialize the database file if it doesn't exist
    with app.app_context():
        create_tables() 
    app.run(debug=True, port=5000)