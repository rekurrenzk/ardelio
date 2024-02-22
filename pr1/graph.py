import serial
import re
import matplotlib.pyplot as plt

ser = serial.Serial('/dev/cu.usbserial-130', 9600)

distances = []

plt.ion()
fig, ax = plt.subplots()
ax.set_title('Distance Measurement')
ax.set_xlabel('Time')
ax.set_ylabel('Distance')

while True:
    try:
        line = ser.readline().decode('utf-8').strip()

        distance_str = re.search(r'\d+', line).group()
        distance = int(distance_str)

        distances.append(distance)

        ax.plot(distances, color='blue')
        plt.pause(0.05)

        ax.relim()
        ax.autoscale_view()

        plt.pause(0.05)

    except KeyboardInterrupt:
        ser.close()
        break

plt.ioff()
plt.show()
