import csv
import numpy as np

#Open data
results = []
with open("Data/transposedcardata.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        results.append(row)
csvfile.close()

#Write each row to a variable
Methane = results[0]
Humidity = results[1]
Temperature = results[2]
Pressure = results[3]
Altitude = results[4]
Latitude = results[5]
Longitude = results[6]

#Write out a bunch of nerd stuff

report = open("Data/Report.txt", "w")

report.write("Average methane: " + str(round(np.mean(Methane), 2)))
report.write("\nMinimum methane: "+ str(round(np.max(Methane), 2)))
report.write("\nMaximum methane: "+ str(round(np.min(Methane), 2)))
report.write("\nLatitude range: "+ str(round(np.max(Latitude) - np.min(Latitude), 2)))
report.write("\nLongitude range: "+ str(round(np.max(Longitude) - np.min(Longitude), 2)))
report.write("\nAverage altitude: "+ str(round(np.mean(Altitude), 2)))

#To be continued...

report.close()
