import tkinter as tk
import cv2
import numpy as np
import time

# Function to detect and count cars in the video
def detect_and_count_cars(video_path):
    # Open the video file
    video = cv2.VideoCapture(video_path)

    # Background subtractor to detect moving objects
    background_subtractor = cv2.createBackgroundSubtractorMOG2()

    car_count_A = 0  # Direction A car count
    car_count_B = 0  # Direction B car count

    while True:
        # Read each frame from the video
        success, frame = video.read()

        # Check if the video ended
        if not success:
            print("Video finished or cannot read video.")
            break

        # Resize the frame for easier processing
        frame = cv2.resize(frame, (640, 360))

        # Apply the background subtractor
        mask = background_subtractor.apply(frame)

        # Remove noise using simple filter
        mask = cv2.medianBlur(mask, 5)

        # Find the shapes (contours) of moving objects
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

         # Loop through all the detected contours
        for contour in contours:
            # Ignore small contours that might be noise
            if cv2.contourArea(contour) > 500:
                # Get the rectangle that fits around the contour
                x, y, w, h = cv2.boundingRect(contour)

                # Draw the rectangle on the original frame
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                # Increase the car count (for simplicity, assume all cars are in Direction A for now)
                # For more complex logic, you can use other detection methods
                car_count_A += 1  # Assume cars are in Direction A for this example

        # Show the car count on the video
        cv2.putText(frame, f"Cars A: {car_count_A}, Cars B: {car_count_B}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Show the original video with rectangles and car count
        cv2.imshow("Car Detection", frame)

        # Wait for 30ms and break if 'q' is pressed
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

     # Release the video and close all windows
    video.release()
    cv2.destroyAllWindows()

    return car_count_A, car_count_B




# Function to detect emergency vehicles using flashing red lights
def detect_emergency_vehicle(video_path):
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video file.")
        exit()

    # Initialize a list to store the red light intensity over time
    light_intensity = []

    # Set a threshold for detecting flashing lights
    flashing_threshold = 5000  # Adjust based on your testing

    frame_skip = 5  # Process every 5th frame
    frame_count = 0
    emergency_direction = None

    while True:
        ret, frame = cap.read()

        if not ret:  # Break if the video ends
            print("Video has ended.")
            break

        frame_count += 1
        if frame_count % frame_skip != 0:
            continue  # Skip this frame and move to the next

        # Convert the frame to HSV for color detection
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Define color range for red lights
        red_lower = np.array([0, 120, 70])
        red_upper = np.array([10, 255, 255])

        # Create a mask for red color
        red_mask = cv2.inRange(hsv, red_lower, red_upper)

        # Count the intensity of the red light in the frame
        red_intensity = cv2.countNonZero(red_mask)  # Number of red pixels


           # Add the intensity to the list
        light_intensity.append(red_intensity)

        # Check if there is enough data to calculate flashing pattern
        if len(light_intensity) > 10:  # Analyze the last 10 frames
            del light_intensity[0]  # Remove the oldest frame's intensity

            # Calculate the change in intensity between consecutive frames
            intensity_changes = [abs(light_intensity[i] - light_intensity[i - 1]) for i in range(1, len(light_intensity))]

            # If the change is above the threshold, it's likely flashing
            if max(intensity_changes) > flashing_threshold:
                print("Flashing red light detected!")
                emergency_direction = "A"  # Assume the emergency vehicle is in Direction A for now
                break

    cap.release()
    cv2.destroyAllWindows()

    return emergency_direction







