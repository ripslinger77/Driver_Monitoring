import subprocess
import time
import re
import math
import keyboard


j = 0

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
        if 'lsm6dsm Accelerometer Non-wakeup: last 50 events' in line or (i>0 and i<51):
            #print(line)
            lines.append(line)
            
                
            i+=1

    #print(lines)
    my_string = lines[50]
    #print(my_string)

    float_values = [float(value) for value in re.findall(r'-?\d+\.\d+', my_string)]

    del float_values[0:2]
    #qprint(float_values)

    

    x, y, z = float_values
    #time.sleep(1)
    print(x,y,z)


    if keyboard.is_pressed("q"):
        break



