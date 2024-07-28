from flask import Flask, request, jsonify
import json
import os
from app.utils import calculate_splits

data_file = 'app/data/data.json'

def read_data():
    if not os.path.exists(data_file):
        return {'users': [], 'expenses': []}
    with open(data_file, 'r') as f:
        return json.load(f)

def write_data(data):
    with open(data_file, 'w') as f:
        json.dump(data, f, indent=4)

def home():
    return jsonify({'message': 'Welcome to the Daily Expenses Sharing Application API'}), 200

def create_user():
    data = read_data()
    new_user = request.json
    new_user['id'] = len(data['users']) + 1
    data['users'].append(new_user)
    write_data(data)
    return jsonify(new_user), 201

def get_user(user_id):
    data = read_data()
    user = next((user for user in data['users'] if user['id'] == user_id), None)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user)

def add_expense():
    data = read_data()
    new_expense = request.json
    new_expense['id'] = len(data['expenses']) + 1
    new_expense['splits'] = calculate_splits(new_expense, new_expense['splits'])
    data['expenses'].append(new_expense)
    write_data(data)
    return jsonify(new_expense), 201

def get_user_expenses(user_id):
    data = read_data()
    user_expenses = [expense for expense in data['expenses'] if expense['user_id'] == user_id]
    for expense in user_expenses:
        expense['splits'] = calculate_splits(expense, expense['splits'])
    return jsonify(user_expenses)

def get_balance_sheet(user_id):
    data = read_data()
    # Add logic to generate balance sheet
    balance_sheet = {}  # Replace with actual balance sheet logic
    return jsonify(balance_sheet)

def init_routes(app):
    app.add_url_rule('/', 'home', home, methods=['GET'])
    app.add_url_rule('/users', 'create_user', create_user, methods=['POST'])
    app.add_url_rule('/users/<int:user_id>', 'get_user', get_user, methods=['GET'])
    app.add_url_rule('/expenses', 'add_expense', add_expense, methods=['POST'])
    app.add_url_rule('/expenses/<int:user_id>', 'get_user_expenses', get_user_expenses, methods=['GET'])
    app.add_url_rule('/balance_sheet/<int:user_id>', 'get_balance_sheet', get_balance_sheet, methods=['GET'])
