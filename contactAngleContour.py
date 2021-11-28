import pandas as pd
import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
import pickle
def fun(x_inp, y_inp):
    df_h = pd.read_csv("BohDataN.csv",header=None)
    df_b = pd.read_csv("BorDataN.csv",header=None)
    df_s = pd.read_csv("CADataN.csv",header=None)

    g = pickle.load(open('predictContactAngle.pkl', 'rb'))
    c_angle = round(g(x_inp,y_inp)[0],0)

    y = df_h.to_numpy()
    x = df_b.to_numpy()
    z = df_s.to_numpy()


    fig, ax = plt.subplots(1, 1)  
    # plots contour lines
    cs = ax.contour(x, y, z, [c_angle])

    ax.set_title('Contour Plot')
    ax.set_xlabel('b')
    ax.set_ylabel('h')
    plt.xlim([0, 3])
    plt.ylim([0, 3])


    x_coord = []
    y_coord = []
    print(np.shape(x_coord))
    for item in cs.collections:
        for i in item.get_paths():
            v = i.vertices
            x = v[:, 0]
            x = np.array(x)
            
            y = v[:, 1]
            y = np.array(y)
        # x_coord = x_coord + x
        # y_coord = y_coord + y
        # for i in x:
            for i in range(len(x)):
                x_coord.append(x[i])
                y_coord.append(y[i])
        print(np.shape(x), np.shape(y))
    # plt.plot(x_coord,y_coord)
    # plt.show()
    # print(x_coord)
    return x_coord,y_coord
    plt.show()