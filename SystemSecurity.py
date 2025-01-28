from flask import Flask, request, jsonify
import jwt
import datetime

app = Flask(__name__)
SECRET_KEY = 'your_secret_key'

# Generate JWT token
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    # You should validate credentials from a database
    if username == 'admin' and password == 'password':
        payload = {
            'username': username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return jsonify({'token': token})

    return jsonify({'message': 'Invalid credentials'}), 401

# Secure route to access sensor data
@app.route('/data', methods=['GET'])
def get_data():
    token = request.headers.get('Authorization')

    if not token:
        return jsonify({'message': 'Token is missing'}), 401

    try:
        # Decode the token
        data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        # Fetch sensor data (this could be real-time data)
        sensor_data = {"ambient_light": 350, "optimal_light_intensity": 150}
        return jsonify(sensor_data)

    except jwt.ExpiredSignatureError:
        return jsonify({'message': 'Token expired'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'message': 'Invalid token'}), 401

if __name__ == '__main__':
    app.run(debug=True)
