import cv2
import datetime
import os
import time 
import av

video = cv2.VideoCapture("C:/D Drive Contents/Driver assist - Internship/Driver_monitoring/Recordings/GOPR0002.MP4")
v = av.open("C:/D Drive Contents/Driver assist - Internship/Driver_monitoring/Recordings/GOPR0002.MP4")
metadata = v.metadata

# Check if the video was loaded correctly
if not video.isOpened():
    print("Error opening video file")

# Get the number of frames in the video
frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

# Get the frame rate (frames per second) of the video
fps = video.get(cv2.CAP_PROP_FPS)

# Calculate the time interval between frames (in seconds)
frame_interval = 1.0 / fps

# Initialize the starting time of the first frame
creation_time = metadata['creation_time']
dt = datetime.datetime.strptime(creation_time, '%Y-%m-%dT%H:%M:%S.%fZ')
start_time = dt - datetime.timedelta(hours=5,minutes=30)

for frame_idx in range(frame_count):
    success, frame = video.read()
    if not success:
        break
    
    # Calculate the timestamp of the current frame
    timestamp = start_time + datetime.timedelta(seconds=frame_interval * frame_idx)

    # Format the timestamp as a string
    timestamp_str = timestamp.strftime("%Y-%m-%d_%H-%M-%S-%f")

    cv2.imwrite(f"C:/D Drive Contents/Driver assist - Internship/Driver_monitoring/Recordings/Ramaiah_frames/frame_{timestamp_str}.jpg", frame)
   

video.release()