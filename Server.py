from flask import Flask
from flask_socketio import SocketIO, emit
import time

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

socketio = SocketIO(app)

# Dummy data for car detection and emergency vehicle detection
cars_A = 10
cars_B = 5
emergency_A = False
emergency_B = True

# Function to simulate car detection and emergency vehicle status
def check_data():
    global cars_A, cars_B, emergency_A, emergency_B
    # This is where you would have the actual car detection and emergency detection logic
    return cars_A, cars_B, emergency_A, emergency_B

# Handle real-time communication with the frontend (GUI)
@socketio.on('get_traffic_data')
def handle_traffic_data(message):
    # Get car counts and emergency vehicle statuses
    cars_A, cars_B, emergency_A, emergency_B = check_data()
    
    # Create a response with the current data
    response = {
        "cars_A": cars_A,
        "cars_B": cars_B,
        "emergency_A": emergency_A,
        "emergency_B": emergency_B
    }
    
    # Emit the data to the client (GUI)
    emit('update_traffic_data', response)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)