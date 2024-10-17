import os
import cv2
import numpy as np
from mtcnn import MTCNN
import tensorflow as tf

# Check for GPU availability
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))

# Configure TensorFlow to use GPU
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    try:
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
    except RuntimeError as e:
        print(e)

# Initialize MTCNN for face detection
detector = MTCNN()

# Function to load images and detect faces
def load_images_and_detect_faces(data_folder):
    faces = []
    labels = []

    for person in os.listdir(data_folder):
        person_folder = os.path.join(data_folder, person)
        if not os.path.isdir(person_folder):
            continue

        for video_folder in os.listdir(person_folder):
            video_frames_folder = os.path.join(person_folder, video_folder)
            if not os.path.isdir(video_frames_folder):
                continue

            for frame_file in os.listdir(video_frames_folder):
                frame_path = os.path.join(video_frames_folder, frame_file)
                img = cv2.imread(frame_path)

                if img is None:
                    print(f"Warning: Could not read image {frame_path}. Skipping.")
                    continue

                # Detect faces
                results = detector.detect_faces(img)
                for result in results:
                    x, y, width, height = result['box']
                    face = img[y:y + height, x:x + width]
                    faces.append(face)
                    labels.append(person)

    return faces, labels

# Load faces and labels from the extracted frames
data_folder = "/content/drive/MyDrive/Techgentsia/Dataset/extracted_frames"  # Replace with your actual folder path
faces, labels = load_images_and_detect_faces(data_folder)

# Display the number of faces detected
print(f"Number of faces detected: {len(faces)}")