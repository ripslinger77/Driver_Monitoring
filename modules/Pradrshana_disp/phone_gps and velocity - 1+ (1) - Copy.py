import subprocess
import csv
import datetime
import time
import keyboard
import math
import pandas as pd
prev_lat = 0
prev_long=0

def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the distance between two points on the Earth's surface using the Haversine formula.
    :param lat1: Latitude of the first point in degrees.
    :param lon1: Longitude of the first point in degrees.
    :param lat2: Latitude of the second point in degrees.
    :param lon2: Longitude of the second point in degrees.
    :return: Distance between the two points in meters.
    """
    R = 6371  # Radius of the Earth in kilometers

    # Convert degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Calculate differences
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    # Apply Haversine formula
    a = math.sin(dlat/2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon/2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = R * c * 1000  # Convert to meters

    return distance

data = pd.read_csv("C:/D Drive Contents/Driver assist - Internship/Driver_monitoring/programs/Pradrshana_disp/gps_iisc_new.csv")
print(data)


j = 0
csv_file=open('C:/D Drive Contents/Driver assist - Internship/Driver_monitoring/Recordings/Pradarshana_disp/speed.csv', mode='w', newline='') 
fieldnames = ['Speed']
writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

# Assuming your DataFrame is named 'df'
for row in data.itertuples(index=False):
    # Access row data using row.column_name
    #print(row.latitude)
    distance = haversine(prev_lat, prev_long, row.latitude, row.longitude)
    prev_lat = row.latitude
    prev_long = row.longitude
    if j == 5:

        print(distance)
        writer.writerow({'Speed': distance})
        j = 0
    j+=1
    #time.sleep(1)
# Open CSV file for writing
'''with open('c:/Users/ashwi/Downloads/gps_data.csv', mode='w', newline='') as csv_file:
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
        distance = haversine(prev_lat, prev_long, float(gps_data['latitude']), float(gps_data['longitude']))
        
        print(distance)
        
        prev_lat = float(gps_data['latitude'])
        prev_long = float(gps_data['longitude'])
        # Wait for 0.033 seconds
        time.sleep(1)'''


