import requests

# Replace this URL with the URL where your server is running
server_url = 'http://127.0.0.1:5000'

# Set the server password
response = requests.post(f'{server_url}/set_password', json={'password': 'your_password'})
print(response.json())

# Attempt to access the server
entered_password = input('Enter the password to access the server: ')
response = requests.post(f'{server_url}/access', json={'password': entered_password})
print(response.json())
