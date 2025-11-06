import subprocess
import time
import re
import math
import keyboard
import csv

prev = 0
j = 0

csv_file=open('C:/D Drive Contents/Driver assist - Internship/Driver_monitoring/Recordings/Pradarshana_disp/Degree.csv', mode='w', newline='') 
fieldnames = ['Bearing','Turning']
writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

writer.writeheader()

while(1):

    # Run ADB command to get orientation data
    output = subprocess.check_output(['adb', 'shell', 'dumpsys', 'sensorservice'])
    i = 0
    lines = []
    # Parse the orientation data from the output
    orientation_data = {}
    for line in output.decode().split('\n'):
        #print(line)
        j=1
        if 'Magnetometer Non-wakeup: last 10 events' in line or (i>0 and i<2):
            #print(line)
            lines.append(line)
            
                
            i+=1

    #print(lines)
    my_string = lines[1]

    float_values = [float(value) for value in re.findall(r'-?\d+\.\d+', my_string)]

    del float_values[0:2]
    #print(float_values)



    x, y, z = float_values

    #print(x,y,z)
    angle_rad = math.atan2(y, x)

    # Convert angle from radians to degrees
    angle_deg = math.degrees(angle_rad)-90

    # Correct for negative angles (atan2 returns values in the range [-pi, pi]
    if angle_deg < 0:
        angle_deg += 360.0

    # Print the angle in degrees
    #print(f"Angle: {angle_deg} degrees")   
    
    #time.sleep(2)
    delta = round(abs(prev - angle_deg),2)
    prev = angle_deg
    #print(delta)
    print(angle_deg)
    if delta==0.0: delta = 0.1
    #print(delta)
    with open("C:/D Drive Contents/Driver assist - Internship/Driver_monitoring/Repos/yolov5/Compass_to_file/compass.txt", "w") as file:
        file.write(str(delta))
    if keyboard.is_pressed("q"):
        break

    writer.writerow({'Bearing': int(angle_deg)})

    '''if delta>3:
        writer.writerow({'Turning': "YES"})'''


