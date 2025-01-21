import socketio
import tkinter as tk

# Initialize the SocketIO client
sio = socketio.Client()

# Create the Tkinter GUI window
root = tk.Tk()
root.title("Traffic Light Control")

# Create labels to display the car counts and emergency vehicle statuses
label_cars_A = tk.Label(root, text="Cars in Direction A: 0")
label_cars_B = tk.Label(root, text="Cars in Direction B: 0")
label_emergency_A = tk.Label(root, text="Emergency in Direction A: No")
label_emergency_B = tk.Label(root, text="Emergency in Direction B: No")

label_cars_A.pack()
label_cars_B.pack()
label_emergency_A.pack()
label_emergency_B.pack()

# Handle the event when data is received from the server
@sio.event
def update_traffic_data(data):
    # Update the labels with the data received from the server
    label_cars_A.config(text=f"Cars in Direction A: {data['cars_A']}")
    label_cars_B.config(text=f"Cars in Direction B: {data['cars_B']}")
    label_emergency_A.config(text=f"Emergency in Direction A: {'Yes' if data['emergency_A'] else 'No'}")
    label_emergency_B.config(text=f"Emergency in Direction B: {'Yes' if data['emergency_B'] else 'No'}")

# Connect to the server
sio.connect('http://localhost:5000')

# Send a request for traffic data
sio.emit('get_traffic_data', {})

# Start the Tkinter main loop
root.mainloop()