from typing import List, Tuple
import numpy as np
import csv
import matplotlib.pyplot as plt

X_INDEX_MAX = 10
Y_INDEX_MAX = 18
POINTS = (X_INDEX_MAX + 1) * (Y_INDEX_MAX + 1)
FIRST_MEASURE_TIME = 7.625
GET_INTERVAL_TIME = 21.9715909
LOG_TIMES = [FIRST_MEASURE_TIME + GET_INTERVAL_TIME * i for i in range(POINTS)]
DATA_FILE_NAME = "data/data_20210712_191745.csv"

magneticFields = [[0.0 for _ in range(X_INDEX_MAX + 1)]
                  for _ in range(Y_INDEX_MAX + 1)]

data = np.genfromtxt(DATA_FILE_NAME,
                     skip_header=1,
                     delimiter=",",
                     usecols=[0, 2])


def latticePoint(i) -> List[int]:
    point = [0, 0]
    point[1] = i // (X_INDEX_MAX + 1)
    if point[1] % 2 == 0:
        point[0] = i % (X_INDEX_MAX + 1)
    else:
        point[0] = X_INDEX_MAX - (i % (X_INDEX_MAX + 1))
    return point


def getNearestValueIndex(list, num):
    return np.abs(np.asarray(list) - num).argmin()


for i, time in enumerate(LOG_TIMES):
    line = getNearestValueIndex(data[:, 0], time)
    magneticField = data[:, 1][line]
    point = latticePoint(i)
    magneticFields[point[1]][point[0]] = magneticField

with open("data/data_lattice_point.csv", "w") as file:
    writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerows(magneticFields)

plt.imshow(magneticFields, cmap=plt.cm.jet, interpolation='nearest')
plt.colorbar()

plt.show()