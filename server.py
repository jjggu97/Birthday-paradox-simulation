from flask import Flask, request, jsonify
import random
import string

app = Flask(__name__)

# Global variable to store the generated password
server_password = None

def generate_random_password():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(12))

@app.route('/set_password', methods=['POST'])
def set_password():
    global server_password
    server_password = request.json.get('password')
    return jsonify({'message': 'Password set successfully'})

@app.route('/access', methods=['POST'])
def access():
    global server_password
    entered_password = request.json.get('password')

    if entered_password == server_password:
        return jsonify({'message': 'Access Confirmed'})
    else:
        return jsonify({'message': 'Access Denied'})

if __name__ == '__main__':
    # Generate a random password when the server starts
    server_password = generate_random_password()
    app.run(debug=True)
