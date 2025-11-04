import subprocess


def gps():
        
    # Run ADB command to get GPS data
    output = subprocess.check_output(['adb', 'shell', 'dumpsys', 'location'])

    # Parse the GPS data from the output
    gps_data = {}
    for line in output.decode().split('\n'):
        #print(line)

        if 'last location=Location' in line:
            #print(line)
            parts = line.strip().split()
            loc = parts[2]
            loc = loc.split(',')
            
            gps_data['latitude'] = loc[0]
            gps_data['longitude'] = loc[1]

    # Print the GPS data
    #print(gps_data)
    #print(type(gps_data))
    lat_long = list(gps_data.values())
    a = ",".join(lat_long)
    #print(a)
    #time.sleep(0.5)
    return(a)


print(gps())