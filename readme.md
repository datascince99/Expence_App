# Daily Expenses Sharing Application API

This is a simple Flask application for managing and sharing daily expenses among users. The application allows you to create users, add expenses, and split expenses among multiple users.

## Project Structure
EXPENSE_APP/
├── app/
│ ├── init.py
│ ├── routes.py
│ ├── utils.py
│ └── data/
│ └── data.json
├── post_expense.py
├── requirements.txt
└── run.py

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

pip install -r requirements.txt

pip install flask

pip install json

pip install requests

python run.py

{
  "message": "Welcome to the Daily Expenses Sharing Application API"
}

python post_expense.py
