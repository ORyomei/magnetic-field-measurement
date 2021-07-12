import matplotlib.pyplot as plt
import numpy as np

dataFileName = "data/data_20210712_191745.csv"
dataLength = sum(1 for i in open(dataFileName, 'r'))

data = np.genfromtxt(dataFileName,
                     skip_header=1,
                     delimiter=",",
                     usecols=[0, 2])

plt.plot(data[:, 0], data[:, 1])
plt.show()
