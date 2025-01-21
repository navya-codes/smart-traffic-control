from flask import Flask
from flask_socketio import SocketIO, emit
# Initialize Flask and SocketIO
app = Flask(__name__)
socketio = SocketIO(app)

# Dummy data for testing (can be replaced with actual detection logic)
traffic_data = {
    "cars_A": 12,
    "cars_B": 8,
    "emergency_A": False,
    "emergency_B": True
}

@app.route('/')
def home():
    return "SocketIO Server is running!"

# Handle traffic data requests from the client
@socketio.on('get_traffic_data')
def send_traffic_data():
    # Send current traffic data to the client
    emit('update_traffic_data', traffic_data)

if __name__ == '__main__':
    print("Starting the server...")
    socketio.run(app, host='0.0.0.0', port=5000)