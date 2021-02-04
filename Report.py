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

#Write out a bunch of nerd stuff

report = open("Data/Report.txt", "w")

report.write("Methane:\n")

report.write("\n\tAverage methane: " + str(round(np.mean(Methane), 2)) + " ppm")
report.write("\n\tMedian methane: " + str(round(np.median(Methane), 2)) + " ppm")
report.write("\n\tMinimum methane: " + str(round(np.min(Methane), 2)) + " ppm")
report.write("\n\tMaximum methane: " + str(round(np.max(Methane), 2)) + " ppm")

report.write("\n\nHumidity:\n")

report.write("\n\tAverage humidity: " + str(round(np.mean(Humidity), 2)) + "%")
report.write("\n\tMedian humidity: " + str(round(np.median(Humidity), 2)) + "%")
report.write("\n\tMinimum humidity: " + str(round(np.min(Humidity), 2)) + "%")
report.write("\n\tMaximum humidity: " + str(round(np.max(Humidity), 2)) + "%")

report.write("\n\nTemperature:\n")

report.write("\n\tAverage temperature: " + str(round(np.mean(Temperature), 2)) + " C")
report.write("\n\tMedian temperature: " + str(round(np.median(Temperature), 2)) + " C")
report.write("\n\tMinimum temperature: " + str(round(np.min(Temperature), 2)) + " C")
report.write("\n\tMaximum temperature: " + str(round(np.max(Temperature), 2)) + " C")

report.write("\n\nPressure:\n")

report.write("\n\tAverage pressure: " + str(round(np.mean(Pressure), 2)) + " hPa")
report.write("\n\tMedian pressure: " + str(round(np.median(Pressure), 2)) + " hPa")
report.write("\n\tMinimum pressure: " + str(round(np.min(Pressure), 2)) + " hPa")
report.write("\n\tMaximum pressure: " + str(round(np.max(Pressure), 2)) + " hPa")

report.write("\n\nLocation:\n")

report.write("\n\tLatitude range: " + str(round(np.max(Latitude) - np.min(Latitude), 2)) + "minutes")
report.write("\n\tLongitude range: " + str(round(np.max(Longitude) - np.min(Longitude), 2)) + "minutes")
report.write("\n\n\tAverage altitude: " + str(round(np.mean(Altitude), 2)) + " m")
report.write("\n\tMinimum altitude: " + str(round(np.min(Altitude), 2)) + " m")
report.write("\n\tMaximum altitude: " + str(round(np.max(Altitude), 2))+ " m\n\n")

dis = 0
for i in range(len(Latitude) - 1):
    dis += math.sqrt((1.85*((Latitude[i + 1] - Latitude[i])) ** 2) + (1.46*((Longitude[i + 1] - Longitude[i])) ** 2) + (0.001*((Altitude[i + 1] - Altitude[i])) ** 2))

report.write(str(round(dis, 2)) + "km")
#To be continued...

report.close()
