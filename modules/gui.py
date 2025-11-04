import cv2
import numpy as np
import pandas as pd
import os

fileroot = "C:/D Drive Contents/Driver assist - Internship/Driver_monitoring/Recordings/frames/"

df = pd.read_csv('C:/Users/manis/OneDrive/Documents/MEGAsync Downloads/merged.csv')

for j in range(len(df['filename'])):

    x = df['filename'][j].split(";")
    
    img = cv2.imread(os.path.join(fileroot, x[0]))
    h,w,c = img.shape

    # Define the video codec, frame size, and frame rate
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        
    fps = 30

    # Initialize the video writer
    out = cv2.VideoWriter('C:/D Drive Contents/Driver assist - Internship/Driver_monitoring/Recordings/frames-vid/output{}.mp4'.format(j), fourcc, fps, (w,h))

    # Loop over the images and write them to the video
    for img_file in x:
        img = cv2.imread(fileroot+img_file)
        out.write(img)

    # Release the video writer
    out.release()