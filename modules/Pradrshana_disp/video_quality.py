import subprocess

# Path to the video file
video_path = "C:/Users/manis/OneDrive/Pictures/Camera Roll/WIN_20230324_14_46_52_Pro.mp4"

# Run the ffprobe command to get the video quality
command = ["ffprobe", "-v", "error", "-select_streams", "v:0",
           "-show_entries", "stream=width,height", "-of", "csv=p=0", video_path]
output = subprocess.check_output(command).decode("utf-8").strip()

# Parse the output to get the width and height of the video
width, height = map(int, output.split(","))

# Print the video quality
print("Video quality: {}x{}".format(width, height))
