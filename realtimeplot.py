import matplotlib.pyplot as plt
import numpy as np

dataFileName = "data/data_20210712_191745.csv"
dataLength = sum(1 for i in open(dataFileName, 'r'))

fig, ax = plt.subplots(1, 1)

while True:
    dataLength = sum(1 for i in open(dataFileName, 'r'))
    data = np.genfromtxt(dataFileName,
                         skip_header=dataLength - 700,
                         delimiter=",",
                         usecols=[0, 2])
    ax.set_xlim((data[:, 0].min(), data[:, 0].max()))
    line, = ax.plot(data[:, 0], data[:, 1], color='blue')
    plt.pause(0.6)
    line.remove()
