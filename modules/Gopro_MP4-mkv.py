import cv2
import datetime
import os
import time 
import av

#use .mkv file for frame extraction
import subprocess

input_file = "C:/Users/manis/OneDrive/Desktop/GOPR0004.MP4"
output_file = "C:/Users/manis/OneDrive/Desktop/Testing_video_to_frames/gopro.mkv"

subprocess.run(["C:/D Drive Contents/Driver assist - Internship/Driver_monitoring/Time-stamp/TimeStamper/TimeStamper/ffmpeg.exe", "-i", input_file, output_file])


# Load the video
video = cv2.VideoCapture("C:/Users/manis/OneDrive/Desktop/Testing_video_to_frames/gopro.mkv")
v = av.open("C:/Users/manis/OneDrive/Desktop/GOPR0004.MP4")
metadata = v.metadata

# Check if the video was loaded correctly
if not video.isOpened():
    print("Error opening video file")

# Get the number of frames in the video
frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

# Get the frame rate (frames per second) of the video
fps = video.get(cv2.CAP_PROP_FPS)

# Get duration of the video
#duration = frame_count/fps

# Calculate the time interval between frames (in seconds)
frame_interval = 1.0 / fps
#print(frame_count,fps)
# Initialize the starting time of the first frame
creation_time = metadata['creation_time']
dt = datetime.datetime.strptime(creation_time, '%Y-%m-%dT%H:%M:%S.%fZ')

start_time = dt - datetime.timedelta(hours=5,minutes=30)

i=0
# Loop through all the frames in the video
for frame_idx in range(frame_count):
    # Read a frame from the video
    ret, frame = video.read()
    i+=1
    
    # Check if the frame was read correctly
    if not ret:
        print("Error reading frame")
        break

    # Calculate the timestamp of the current frame
    timestamp = start_time + datetime.timedelta(seconds=frame_interval * frame_idx)

    # Format the timestamp as a string
    timestamp_str = timestamp.strftime("%Y-%m-%d_%H-%M-%S-%f")

    # Save the frame as an image
    cv2.imwrite(f"C:/D Drive Contents/Driver assist - Internship/Driver_monitoring/Recordings/Ramaiah_frames/frame_{timestamp_str}.jpg", frame)
print(i)
# Release the video
video.release()


