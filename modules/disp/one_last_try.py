from moviepy.editor import VideoFileClip, concatenate_videoclips

# Set up the video file paths
video1_path = "C:/Users/ashwi/Desktop/map_iisc.mp4"
video2_path = "C:/Users/ashwi/Desktop/Iisc_New_5Min.mp4"
#video3_path = "video3.mp4"

# Load the video clips using moviepy
video1 = VideoFileClip(video1_path)
video2 = VideoFileClip(video2_path)
#video3 = VideoFileClip(video3_path)

# Set the video clips to loop
video1 = video1.loop(-1)
video2 = video2.loop(-1)
#video3 = video3.loop(-1)

# Concatenate the video clips horizontally
final_clip = concatenate_videoclips([video1, video2], method="compose")

# Play the concatenated video clip
final_clip.preview()
input("Press Enter to exit...")
