import cv2

# Function to capture image from webcam
def capture_image():
    cap = cv2.VideoCapture(0)  # 0 is usually the default webcam

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return None

    # Capture a single frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame.")
        return None

    # Release the webcam
    cap.release()

    return frame

# Capture image from webcam
frame = capture_image()

if frame is not None:
    # Display the captured image using OpenCV
    cv2.imshow("Captured Image", frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
