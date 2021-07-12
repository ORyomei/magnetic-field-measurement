from magnetic_field_measurement.sensor_receiver import SenserReceiver
import datetime
import csv
import time
import matplotlib.pyplot as plt

initialTime = datetime.datetime.now()
dataFileName = "data/data_{}.csv".format(initialTime.strftime('%Y%m%d_%H%M%S'))
sensor = SenserReceiver()
with open(dataFileName, "a") as file:
    writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(["Elapsed time", "Datetime", "Magnetic field"])

while True:
    now = datetime.datetime.now()
    elapsedTime = (now - initialTime).total_seconds()
    magneticFiled = float(sensor.read())
    with open(dataFileName, "a") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
        writeRow = [elapsedTime, str(now), magneticFiled]
        writer.writerow(writeRow)
        print(writeRow)
        time.sleep(0.5)
