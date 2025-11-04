from moviepy.editor import *
import numpy as np
import pyautogui


# Load videos
video1 = VideoFileClip("C:/D Drive Contents/Driver assist - Internship/Driver_monitoring/Recordings/Pradarshana_disp/map_iisc.mp4")
video2 = VideoFileClip("C:/D Drive Contents/Driver assist - Internship/Driver_monitoring/Recordings/Pradarshana_disp/Iisc New 5Min.mp4")
video3 = VideoFileClip("C:/D Drive Contents/Driver assist - Internship/Driver_monitoring/Recordings/Pradarshana_disp/Img 0853.mp4")
screen_size = pyautogui.size()
screen_height = screen_size[0]
screen_width = screen_size[1]

# Set video dimensions
width = 630
height = screen_height
print(height)

# Resize videos to half width and half height
video1 = video1.resize((width, height))
video2 = video2.resize((width, height))
video3 = video3.resize((width, height))

# Set videos side by side
side_by_side = CompositeVideoClip([
    video1.set_position((0,0)),
    video2.set_position((1,1)),
    video3.set_position((0.5,1))
], size=(width, height))

# Set final video duration as the maximum duration among the three videos
final_duration = max(video1.duration, video2.duration, video3.duration)
side_by_side = side_by_side.set_duration(final_duration)

# Write merged video to file
side_by_side.write_videofile('C:/D Drive Contents/Driver assist - Internship/Driver_monitoring/Recordings/Pradarshana_disp/merged_video.mp4', codec='libx264')
