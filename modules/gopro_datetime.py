import cv2
import os
import time

# Open the video file
video_file = "C:/D Drive Contents/Driver assist - Internship/Driver_monitoring/Recordings/GOPR0002.MP4"
cap = cv2.VideoCapture(video_file)

# Get the video properties
fps = cap.get(cv2.CAP_PROP_FPS)
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
duration = frame_count / fps

# Get the starting time of the video
start_time = time.time()

# Extract and rename each frame
for i in range(frame_count):
    # Read the next frame
    ret, frame = cap.read()

    # Calculate the relative time for the frame
    relative_time = time.time() - start_time

    # Format the time stamp as HH:MM:SS
    time_stamp = time.strftime("%H:%M:%S", time.gmtime(relative_time))

    # Add the fractional second to the time stamp
    fractional_second = (relative_time % 1) * 1000
    time_stamp = f"{time_stamp}.{int(fractional_second):03}"

    # Save the frame with the time stamp as the file name
    frame_file = f"C:/D Drive Contents/Driver assist - Internship/Driver_monitoring/Recordings/Ramaiah_frames/{time_stamp}.jpg"
    cv2.imwrite(frame_file, frame)

# Release the video capture object
cap.release()











