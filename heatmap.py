import pandas as pd
import matplotlib.pyplot as plt

# Remove once we have GPS data
import math
import random

# Initialize plots
fig1 = plt.figure()
fig2 = plt.figure()
ax1 = fig1.gca(projection='3d')
ax2 = fig2.gca(projection='3d')

# Add once we have methane data
# fig3 = plt.figure()
# ax3 = fig3.add_subplot(111, projection='3d')

# Remove once we have GPS data
x = []
y = []

# Load data. I used the raw data from output.txt for testing
data = pd.read_csv('DroneTestData.csv')

altitude = []

# Remove once we have GPS data
for i in range(3044):
    x.append(i % 50)
    y.append(math.floor(i / 50))

# Columns = pressure, temperature, humidity, time(not used), methane(need methane data), x(need GPS data), y(need GPS data)
pressure = data.iloc[:, 0].tolist()
temperature = data.iloc[:,1].tolist()
humidity = data.iloc[:,2].tolist()

# Add once we have GPS and methane data
#methane = data.iloc[:,4].tolist()
#x = data.iloc[:,5].tolist()
#y = data.iloc[:,6].tolist()

# Get altitude from pressure
for i in range(len(pressure)):
    altitude.append((((1013.25/pressure[i])**(1/5.257)-1)*(temperature[i]+273.15))/0.0065)

# Plot the data to two different plots
ax1.scatter(x, y, altitude, c=temperature)
ax1.set_title("Temperature Heatmap")
ax1.set_xlabel("x (m)")
ax1.set_ylabel("y (m)")
ax1.set_zlabel("altitude (m)")
ax2.scatter(x, y, altitude, c=humidity)
ax2.set_title("Humidity Heatmap")
ax2.set_xlabel("x (m)")
ax2.set_ylabel("y (m)")
ax2.set_zlabel("altitude (m)")
#ax3.scatter(x, y, altitude, c=methane)
#ax3.set_title("Methane Heatmap")
#ax3.set_xlabel("x (m)")
#ax3.set_ylabel("y (m)")
#ax3.set_zlabel("altitude (m)")
#ax3.text2D(0.05, 0.07, "Colour = Methane")
#plt.show()

# Rotate the plot to look nicer
ax1.view_init(35, 190)
ax2.view_init(35, 190)
#ax3.view_init(30, 135)
plt.draw()
