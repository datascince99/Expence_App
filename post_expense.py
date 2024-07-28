import requests
import json

# URL of the Flask API endpoint
url = 'http://127.0.0.1:5000/expenses'

# Example data to post (Equal Split)
data_equal = {
    "user_id": 1,
    "amount": 3000,
    "split_method": "exact",
    "splits": [
        {"user_id": 1, "amount": 1000},
        {"user_id": 2, "amount": 1000},
        {"user_id": 3, "amount": 1000}
    ]
}

# Example data to post (Exact Split)
data_exact = {
    "user_id": 1,
    "amount": 3000,
    "split_method": "exact",
    "splits": [
        {"user_id": 1, "amount": 1000},
        {"user_id": 2, "amount": 1000},
        {"user_id": 3, "amount": 1000}
    ]
}

# Example data to post (Percentage Split)
data_percentage = {
    "user_id": 1,
    "amount": 3000,
    "split_method": "percentage",
    "splits": [
        {"user_id": 1, "percentage": 50},
        {"user_id": 2, "percentage": 30},
        {"user_id": 3, "percentage": 20}
    ]
}

# Choose which data to send
data = data_exact  # change to data_exact or data_percentage as needed

# Send the POST request
response = requests.post(url, headers={'Content-Type': 'application/json'}, data=json.dumps(data))

# Print the response
print(response.status_code)
print(response.json())
