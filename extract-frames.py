import cv2
import os

def extract_frames(video_path, output_dir, skip_frames=5):
    """
    Extract frames from a video and save them to the output directory.
    Parameters:
    - video_path: Path to the video file.
    - output_dir: Directory to save the frames.
    - skip_frames: Number of frames to skip between saves.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    saved_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % skip_frames == 0:
            frame_file = os.path.join(output_dir, f"frame_{saved_count}.jpg")
            cv2.imwrite(frame_file, frame)
            saved_count += 1

        frame_count += 1

    cap.release()
    print(f"Extracted {saved_count} frames from {video_path}")

# Extract frames for all videos in the dataset
video_folder = "/content/drive/MyDrive/Techgentsia/Dataset/files"  # Root folder containing subfolders of each person
output_folder = "/content/drive/MyDrive/Techgentsia/Dataset/extracted_frames"  # Folder to save extracted frames

for person in os.listdir(video_folder):
    person_folder = os.path.join(video_folder, person)
    if os.path.isdir(person_folder):  # Ensure it's a folder
        for video in os.listdir(person_folder):
            video_path = os.path.join(person_folder, video)
            output_dir = os.path.join(output_folder, person, video.replace('.mp4', ''))
            extract_frames(video_path, output_dir)