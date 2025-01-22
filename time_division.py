

count_A = 15  #  count for Direction A
count_B = 45 #  count for Direction B

# Initialize emergency detection status
emergency_detected = False # Change to True if an emergency vehicle is detected
emergency_direction = None  # 'A' or 'B' if emergency detected

# Function to calculate green light durations
def calculate_green_times(count_A, count_B):
    total_cars = count_A + count_B
    if total_cars == 0:  # Avoid division by zero
        return 30, 30  # Default green times for both directions
    time_A = (count_A / total_cars) * 60  # Green time for Direction A
    time_B = (count_B / total_cars) * 60  # Green time for Direction B
    return int(time_A), int(time_B)

# Main function for traffic light control
def traffic_light_control():
    global emergency_detected, emergency_direction
    if emergency_detected:
        print(f"Emergency detected in Direction {emergency_direction}.")
        print(f"Direction {emergency_direction}: Green Light (Priority)")
        print(f"Other directions: Red Light")
    else:
        # Calculate green light times based on vehicle counts
        green_time_A, green_time_B = calculate_green_times(count_A, count_B)
        print(f"Direction A: Green Light ({green_time_A}s)")
        print(f"Direction B: Green Light ({green_time_B}s)")

# Simulating traffic light control
print("Starting Traffic Light Simulation...\n")
traffic_light_control()  # Run the traffic light control function