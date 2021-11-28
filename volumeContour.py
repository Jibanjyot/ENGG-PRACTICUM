import pandas as pd
import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

def shapeIndex(x_input,y_input):
    df_h = pd.read_csv("BohDataN.csv",header=None)
    df_b = pd.read_csv("BorDataN.csv",header=None)
    df_s = pd.read_csv("ShapeIndexDataN.csv",header=None)

    y = df_h.to_numpy()
    x = df_b.to_numpy()
    z = df_s.to_numpy()


    fig, ax = plt.subplots(1, 1)  
    cs = ax.contour(x, y, z, [1])


    x_coord = []
    y_coord = []
    # print(np.shape(x_coord))
    for item in cs.collections:
        for i in item.get_paths():
            v = i.vertices
            x = v[:, 0]
            x = np.array(x)
            
            y = v[:, 1]
            y = np.array(y)
            for i in range(len(x)):
                x_coord.append(x[i])
                y_coord.append(y[i])
            # print(np.shape(x), np.shape(y))

    return x_coord,y_coord
