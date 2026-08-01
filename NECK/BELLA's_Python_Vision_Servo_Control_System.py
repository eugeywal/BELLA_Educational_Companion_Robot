# Import OpenCV library for real-time visual frame processing
import cv2

# Import NumPy library for numerical array operations and interpolation mapping
import numpy as np

# Import PySerial library to handle hardware communication with Arduino
import serial

# Import time module to manage execution delays during initialization
import time

# Attempt to establish a serial connection with the Arduino Uno board
try:
    # Initialize serial port COM10 at a high baud rate of 115200 with 1-second timeout
    arduino = serial.Serial('COM10', 115200, timeout=1)
    
    # Pause execution for 2 seconds to allow Arduino microcontroller to reset and warm up
    time.sleep(2)
    
    # Print success confirmation message to console
    print("Connected to Arduino successfully!")

except Exception as e:
    # Catch any connection exceptions and display error message
    print("Unable to connect to Arduino:", e)
    
    # Set arduino variable to None to allow offline processing without hardware crash
    arduino = None

# Open the primary computer webcam video stream (device index 0)
cap = cv2.VideoCapture(0)

# Set the webcam capture resolution width to 640 pixels for faster execution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)

# Set the webcam capture resolution height to 480 pixels to optimize CPU usage
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Define the lower threshold bound for target color tracking in HSV space (Blue color)
lower_blue = np.array([90, 50, 50])

# Define the upper threshold bound for target color tracking in HSV space (Blue color)
upper_color_bounds = np.array([130, 255, 255])

# Initialize default target angle for the servo motor to center (90 degrees)
servo_angle = 90

# Variable to track the previously transmitted angle to minimize redundant writes
last_angle = -1

# Minimum angle variation threshold required to trigger a new serial command
ANGLE_THRESHOLD = 2

# Main execution loop for tracking and continuous control
while True:
    # Read a frame from the webcam stream
    ret, frame = cap.read()
    
    # Exit loop if the video feed fails to stream or frame is invalid
    if not ret:
        break

    # Apply Gaussian Blur filter to smooth image noise and reduce false positives
    frame = cv2.GaussianBlur(frame, (5, 5), 0)
    
    # Flip the image horizontally to create a natural mirror-view effect
    frame = cv2.flip(frame, 1)
    
    # Extract dimensions (height and width) from the captured frame
    height, width, _ = frame.shape
    
    # Calculate the horizontal center position of the screen display
    center_screen_x = width // 2

    # Convert BGR color space of the frame to HSV color space for color filtering
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Create a binary mask isolating pixels falling within the target HSV color range
    mask = cv2.inRange(hsv, lower_blue, upper_color_bounds)
    
    # Perform morphological erosion to eliminate background noise particles
    mask = cv2.erode(mask, None, iterations=2)
    
    # Perform morphological dilation to restore original object dimensions after erosion
    mask = cv2.dilate(mask, None, iterations=2)

    # Locate external boundary contours of the detected binary shapes
    contours, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Process object tracking logic if at least one valid contour is detected
    if len(contours) > 0:
        # Identify the contour with the largest geometric surface area
        c = max(contours, key=cv2.contourArea)
        
        # Calculate the minimum enclosing circle center coordinates and radius around contour
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        
        # Verify object validity by ensuring its radius exceeds noise threshold (25 pixels)
        if radius > 25:
            # Draw outer tracking circle around the detected object on display frame
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            
            # Draw center point marker inside detected object radius
            cv2.circle(frame, (int(x), int(y)), 5, (0, 0, 255), -1)
            
            # Interpolate object X coordinate (0 to frame width) into Servo Angle range (180 to 0)
            servo_angle = int(np.interp(x, [0, width], [180, 0]))

            # Send position updates over serial if Arduino hardware connection is live
            if arduino is not None:
                # Transmit command only if positional difference meets or exceeds threshold
                if abs(servo_angle - last_angle) >= ANGLE_THRESHOLD:
                    # Send encoded string message containing target angle over serial line
                    arduino.write(f"{servo_angle}\n".encode())
                    
                    # Update stored previous angle reference
                    last_angle = servo_angle

    # Draw vertical reference axis down the middle of the camera feed
    cv2.line(frame, (center_screen_x, 0), (center_screen_x, height), (255, 0, 0), 2)
    
    # Render active servo angle readout onto visual frame interface
    cv2.putText(frame, f"Servo Angle: {servo_angle} deg", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # Render interactive graphical window containing processed camera output
    cv2.imshow("AI Vision -> Arduino Servo Control", frame)

    # Intercept keyboard event and break processing loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture hardware stream resource
cap.release()

# Close active serial port connection safely if initialized
if arduino:
    arduino.close()

# Destroy all opened OpenCV graphical windows
cv2.destroyAllWindows()