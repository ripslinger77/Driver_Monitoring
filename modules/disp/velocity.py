import subprocess
import time
import re
import math
import keyboard
import csv
velocity = []
while(True):

    # Run ADB command to get orientation data
    output = subprocess.check_output(['adb', 'shell', 'dumpsys', 'sensorservice'])
    i = 0
    lines = []
    # Parse the orientation data from the output
    orientation_data = {}
    for line in output.decode().split('\n'):
       # print(line)
        line=line.lower()
        j=1
        if 'accelerometer non-wakeup: last 50 events' in line or (i>0 and i<4):
            #print(line)
            lines.append(line)
            
                
            i+=1

    #print(lines)
    my_string = lines[1]+lines[2]+lines[3]
    #print(my_string)
    
    float_values = [float(value) for value in re.findall(r'-?\d+\.\d+', my_string)]
    #print(float_values)
    t1 = float_values[0]
    t2 = float_values[5]
    t3 = float_values[10]

    #print(t1,t2,t3)

    del float_values[0:2]
    del float_values[3:5]
    del float_values[6:8]

    #print(float_values)
    acc1 = math.sqrt(float_values[0]**2 + float_values[1]**2)
    acc2 = math.sqrt(float_values[3]**2 + float_values[4]**2)
    acc3 = math.sqrt(float_values[6]**2 + float_values[7]**2)
    #print(acc1,acc2,acc3)
    v =  (acc1+acc2)/2 * (t2-t1) + (acc2+acc3)/2 * (t3-t2)
    print(v)
    velocity.append(v)
        
    if keyboard.is_pressed("q"):
        break
print(velocity)
with open('A:/endresult/velocity.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Velocity (m/s)'])
        for v in velocity:
            writer.writerow([v])



