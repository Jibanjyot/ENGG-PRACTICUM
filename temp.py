import pickle

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import splev, splrep
from scipy import interpolate
from sklearn import neighbors, datasets

g = pickle.load(open('predictContactAngle.pkl', 'rb'))
result = g(1.5, 1.5)
print(result[0])
df = pd.read_excel("boundaryPoints_2.xlsx", header=None)
x_points = list(df.iloc[:, 0])
y_points = list(df.iloc[:, 1])
# print(x_points)
# print(y_points)
tck = splrep(x_points, y_points)

c_angle_input = round(result[0], 1)

b_star_array = np.arange(0, 4, 0.01)
h_star_array = np.arange(0, 4, 0.01)

contour_b = [0]
contour_h = [0]

df = pd.read_csv("boundaryThinFilmData.csv", header=None)
x_thinFilm = list(df.iloc[1:, 0])
y_thinFilm = list(df.iloc[1:, 1])
tck1 = interpolate.splrep(x_thinFilm, y_thinFilm)

for j in h_star_array:
    for i in b_star_array:
        y_out1 = interpolate.splev(i, tck1)
        if j < y_out1:
            continue
        y_out = interpolate.splev(i, tck)
        if y_out-j < 0:
            continue
        contactangle = round(g(i, j)[0], 1)
        if contactangle == c_angle_input:
            contour_b.append(i)
            contour_h.append(j)

print(contour_b, contour_h)
