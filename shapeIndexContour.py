from turtle import shape
import pandas as pd
import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
import pickle
def shapeIndex(x_input,y_input):
    df_h = pd.read_csv("BohDataN.csv",header=None)
    df_b = pd.read_csv("BorDataN.csv",header=None)
    df_s = pd.read_csv("ShapeIndexDataN.csv",header=None)

    y = df_h.to_numpy()
    x = df_b.to_numpy()
    z = df_s.to_numpy()

    y_1 = df_h.to_numpy()
    x_1 = df_b.to_numpy()

    s_Index=pickle.load(open('predictShapeIndex.pkl','rb'))
    shape_index = s_Index(x_input,y_input)[0][0]
    
    fig, ax = plt.subplots(1, 1)  
    min_dist = 1
    shape_index_to_be_taken = shape_index
    shape_index_array = np.linspace(shape_index-0.3,shape_index+0.3,50)
    
    for shape_index in shape_index_array:
        cs = ax.contour(x_1, y_1, z, [shape_index])
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
                    # x_coord.append(x[i])
                    # y_coord.append(y[i])
                    if (x_input-x[i])*(x_input-x[i]) + (y_input-y[i])*(y_input-y[i])<min_dist:
                        min_dist = (x_input-x[i])*(x_input-x[i]) + (y_input-y[i])*(y_input-y[i])
                        shape_index_to_be_taken = shape_index
                # print(np.shape(x), np.shape(y))
    
    cs = ax.contour(x_1, y_1, z, [shape_index_to_be_taken])
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
            

    return x_coord,y_coord


