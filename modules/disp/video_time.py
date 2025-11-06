from moviepy.video.io.VideoFileClip import VideoFileClip

# Load the video file
clip = VideoFileClip("C:/D Drive Contents/Driver assist - Internship/Driver_monitoring/Recordings/GOPR0067.MP4")

# Get the duration of the video in seconds
duration = clip.duration

# Print the duration
print(f"The duration of the video is {duration} seconds.")
