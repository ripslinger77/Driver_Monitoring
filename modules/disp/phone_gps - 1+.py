import subprocess
import csv
import datetime
import time
import keyboard

# Open CSV file for writing
with open('C:/D Drive Contents/Driver assist - Internship/Driver_monitoring/programs/Pradrshana_disp/gps_data.csv', mode='w', newline='') as csv_file:
    fieldnames = ['timestamp', 'latitude', 'longitude']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    # Write headers
    writer.writeheader()

    # Continuously get GPS values and write to CSV
    while True:

        if keyboard.is_pressed("q"):
            break

        # Run ADB command to get GPS data
        output = subprocess.check_output(['adb', 'shell', 'dumpsys', 'location'])

        # Parse the GPS data from the output
        gps_data = {}
        for line in output.decode().split('\n'):
            if 'last location=Location' in line:
                parts = line.strip().split()
                loc = parts[2]
                loc = loc.split(',')
                gps_data['latitude'] = loc[0]
                gps_data['longitude'] = loc[1]

            

        print(gps_data)

        # Get timestamp
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Write GPS data to CSV
        writer.writerow({'timestamp': timestamp, 'latitude': gps_data['latitude'], 'longitude': gps_data['longitude']})

        
        # Wait for 0.033 seconds
        #time.sleep(0.033)

        
