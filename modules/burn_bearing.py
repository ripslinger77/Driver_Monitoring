import cv2
import time

import pandas as pd
import os

fileroot = "C:/D Drive Contents/Driver assist - Internship/Driver_monitoring/Recordings/frames-vid/"
filedest = "C:/D Drive Contents/Driver assist - Internship/Driver_monitoring/Recordings/frames-vid_up/"
df = pd.read_csv('C:/Users/manis/OneDrive/Documents/MEGAsync Downloads/merged.csv')

for j in range(len(df['filename'])):

    # open the video file
    video = cv2.VideoCapture(fileroot+'output{}.mp4'.format(j))

    # set the font and font scale
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_thickness = 10

    # get the video properties
    frame_width = int(video.get(3))
    frame_height = int(video.get(4))

    fps = int(video.get(cv2.CAP_PROP_FPS))

    # set the output video file
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # or another fourcc code
    out = cv2.VideoWriter(filedest+'output{}.mp4'.format(j), fourcc, fps, (frame_width, frame_height))

    # read the frames
    while True:
        ret, frame = video.read()
        if not ret:
            break
        
        # add the value to the frame
        value = df['Bearing'][j]  # replace with the desired value
        cv2.putText(frame, str(value), (10, 200), font, font_scale, (0, 0, 255), font_thickness)

    out.write(frame)
        

    # release the video
    video.release()


