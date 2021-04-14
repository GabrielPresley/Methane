import csv
import numpy as np
import math

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
Time = results[7]

#Write out a bunch of nerd stuff
report = open("Data/Report.txt", "w")

for element, datas, unit in zip(["Methane:","Humidity:","Temperature:","Pressure:"], [results[0],results[1],results[2],results[3]], [" ppm","%","*C"," hPa"]):
    report.write(element)
    report.write("\n\tAverage "+ element + str(round(np.mean(datas), 2)) + unit)
    report.write("\n\tMedian  "+ element + str(round(np.median(datas), 2)) + unit)
    report.write("\n\tMinimum "+ element + str(round(np.min(datas), 2)) + unit)
    report.write("\n\tMaximum "+ element + str(round(np.max(datas), 2)) + unit + "\n\n")
#
report.write("Location:")

report.write("\n\tLatitude range: " + str(round(np.max(Latitude) - np.min(Latitude), 2)) + "minutes")
report.write("\n\tLongitude range: " + str(round(np.max(Longitude) - np.min(Longitude), 2)) + "minutes")
report.write("\n\n\tAverage altitude: " + str(round(np.mean(Altitude), 2)) + "m")
report.write("\n\tMinimum altitude: " + str(round(np.min(Altitude), 2)) + "m")
report.write("\n\tMaximum altitude: " + str(round(np.max(Altitude), 2))+ "m\n\n")

dis = 0
for i in range(len(Latitude) - 1):
    dis += math.sqrt((1.85*((Latitude[i + 1] - Latitude[i])) ** 2) + (1.46*((Longitude[i + 1] - Longitude[i])) ** 2) + (0.001*((Altitude[i + 1] - Altitude[i])) ** 2))

speed = dis * 1000 / Time[-1]

report.write("Total distance travelled: " + str(round(dis, 2)) + "km")
report.write("\nAverage speed: " + str(round(speed, 2)) + "m/s (" + str(round(speed * 3.6, 2)) + "km/h, " + str(round(speed * 2.237, 2)) + "mph)")
#To be continued...

report.close()
