import tkinter as tk
import time

# Function to simulate traffic light changes
def update_traffic_lights(direction_A, direction_B):
    # Clear the canvas (reset the traffic lights)
    canvas.delete("all")
    
    # Create circles (representing the lights) on the canvas for each direction
    if direction_A == "green":
        canvas.create_oval(50, 50, 150, 150, fill="green", outline="black")
    else:
        canvas.create_oval(50, 50, 150, 150, fill="red", outline="black")
    
    if direction_B == "green":
        canvas.create_oval(250, 50, 350, 150, fill="green", outline="black")
    else:
        canvas.create_oval(250, 50, 350, 150, fill="red", outline="black")
    
    # Update the canvas (force the display to update)
    window.update()

# Main function to set up the GUI
def main():
    global canvas, window
    # Create a window for the GUI
    window = tk.Tk()
    window.title("Smart Traffic Control System")

    # Create a canvas to draw the traffic lights
    canvas = tk.Canvas(window, width=400, height=200)
    canvas.pack()

    # Example simulation: Simulating 3 seconds green for A, then 3 seconds green for B
    for _ in range(3):
        update_traffic_lights("green", "red")
        time.sleep(1)  # Pause for a moment (simulate time)
        window.update()
    
    for _ in range(3):
        update_traffic_lights("red", "green")
        time.sleep(1)
        window.update()

    # Start the Tkinter main loop
    window.mainloop()

# Run the main function
if __name__ == "__main__":
    main()