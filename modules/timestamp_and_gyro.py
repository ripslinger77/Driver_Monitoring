import cv2
import time
import numpy as np
import pyrealsense2 as rs

# Initialize the RealSense camera and start streaming
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
config.enable_stream(rs.stream.gyro, rs.format.motion_xyz32f, 200)


pipeline.start(config)

# Create a font for the timestamp text
font = cv2.FONT_HERSHEY_SIMPLEX

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

    gyro_data = gyro_frame.as_motion_frame().get_motion_data()
    gyro_x, gyro_y, gyro_z = gyro_data.x, gyro_data.y, gyro_data.z
    
    
    # Draw the timestamp text onto the color image
    cv2.putText(color_image, timestamp, (10, 30), font, 1, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.putText(color_image, gyro_x, (10, 30), font, 1, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.putText(color_image, gyro_y, (10, 30), font, 1, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.putText(color_image, gyro_z, (10, 30), font, 1, (0, 0, 255), 2, cv2.LINE_AA)
    
    # Show the resulting image with the timestamp overlay
    cv2.imshow("RealSense Camera", color_image)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
cv2.destroyAllWindows()