import cv2
import time
import numpy as np
import pyrealsense2 as rs

import phone_gps as gp
import phone_compass as com

# Initialize the RealSense camera and start streaming
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
config.enable_stream(rs.stream.gyro)

pipeline.start(config)

# Create a font for the timestamp text
font = cv2.FONT_HERSHEY_SIMPLEX

# Initialize the compass values and time elapsed since last update
compass = com.compass()
last_compass_update = time.time()

# Main loop to process camera frames
while True:
    
    # Wait for a new camera frame
    frames = pipeline.wait_for_frames()
    color_frame = frames.get_color_frame()
    depth_frame = frames.get_depth_frame()

    gyro_frame = frames.first_or_default(rs.stream.gyro)
    
    # Convert the color frame to a NumPy array for processing
    color_image = np.asanyarray(color_frame.get_data())
    
    # Get the current timestamp and format it as a string
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    
    # Update compass values if more than 1 second has elapsed since last update
    if time.time() - last_compass_update > 1:
        compass = com.compass()
        last_compass_update = time.time()
    
    # Draw the timestamp and compass text onto the color image
    cv2.putText(color_image, timestamp, (10, 30), font, 1, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.putText(color_image, str(compass), (10, 60), font, 1, (0, 0, 255), 2, cv2.LINE_AA)
    
    # Show the resulting image with the timestamp and compass overlay
    cv2.imshow("RealSense Camera", color_image)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
