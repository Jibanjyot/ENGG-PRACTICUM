import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import splev, splrep
from scipy import interpolate
from sklearn import neighbors, datasets
import pickle
import math

# def fun(x_inp, y_inp):

#     df = pd.read_excel("boundaryPoints_2.xlsx", header=None)
#     x_points = list(df.iloc[:, 0])
#     y_points = list(df.iloc[:, 1])
#     # print(x_points)
#     # print(y_points)
#     tck = splrep(x_points, y_points)

#     # df_h = pd.read_csv("BohDataN.csv",header=None)
#     # df_b = pd.read_csv("BorDataN.csv",header=None)
#     # df_c = pd.read_csv("CADataN.csv",header=None)

#     # for i in range(0,324):
#     #     df_h[i] = df_h[i].fillna(99999)
#     #     df_b[i] = df_b[i].fillna(99999)
#     #     df_c[i] = df_c[i].fillna(99999)

#     # x1 = []
#     # x2 = []
#     # y1 = []
#     # for i in range(0,150):
#     #     for j in range(0,324):
#     #         if(df_h.iloc[i,j]==99999):
#     #             continue
#     #         else:
#     #             x2.append(df_h.iloc[i,j])
#     #             x1.append(df_b.iloc[i,j])
#     #             y1.append(df_c.iloc[i,j])

#     # x2 ia hstar
#     # x1 is b star
#     # x = np.array(x1)
#     # y = np.array(x2)
#     # xg, yg = np.meshgrid(x, y,indexing='ij', sparse=True)
#     # z = np.array(y1)
#     # g = interpolate.interp2d(x, y, z, kind='quintic')

#     g = pickle.load(open('predictContactAngle.pkl', 'rb'))
#     result = g(x_inp, y_inp)

#     x_input = x_inp
#     y_input = y_inp
#     y_out = interpolate.splev(x_input, tck)
#     if y_out-y_input < 0:
#         yo = 1
#         #print("Unstable region")
#         # print(y_out,y_input)
#     elif (x_input < 0 and y_input > 0) or (x_input < 0 and y_input < 0) or (x_input > 0 and y_input < 0):
#         # print("Unstable region")
#         # print(y_out,y_input)
#         yoyo = 2

#     else:
#         #print("stable region")
#         #print("expected output",y_out)
#         #print("given output",y_input)
#         contactAngle = g(x_input, y_input)
#         ##warnings.filterwarnings("ignore", category=RuntimeWarning)
#         # we need to output znew[0]
#         # print(round(contactAngle[0],0))
#     if result[0]>=95:
#         b_star_array = np.arange(0, 1, 0.005)
#         h_star_array = np.arange(0, 2, 0.005)
#     else:
#         b_star_array = np.arange(0, 4, 0.01)
#         h_star_array = np.arange(0, 4, 0.01)
#     # h_input = 1.5
#     c_angle_input = round(contactAngle[0], 0)
#     # print(b_star_array)
#     contour_b = []
#     contour_h = []

#     df = pd.read_csv("boundaryThinFilmData.csv", header=None)
#     x_thinFilm = list(df.iloc[1:, 0])
#     y_thinFilm = list(df.iloc[1:, 1])
#     tck1 = interpolate.splrep(x_thinFilm, y_thinFilm)

#     for j in h_star_array:
#         for i in b_star_array:
#             y_out1 = interpolate.splev(i, tck1)
#             if j < y_out1:
#                 continue
#             y_out = interpolate.splev(i, tck)
#             if y_out-j < 0:
#                 continue
#             contactangle = round(g(i, j)[0], 1)
#             if contactangle == c_angle_input:
#                 contour_b.append(i)
#                 contour_h.append(j)

#     # print(contour_b)
#     # print(contour_h)
#     fin_contourA = []
#     fin_contourB = []
#     x = 0
#     y = 0
#     x_an = 0
#     y_an = 0
#     num = 0
#     ln = len(contour_b)
#     while num < ln:
#         mn = float('inf')
#         for i, j in zip(contour_b, contour_h):
#             if (i-x)*(i-x)+(j-y)*(j-y) < mn:
#                 mn = (i-x)*(i-x)+(j-y)*(j-y)
#                 x_an = i
#                 y_an = j
#         contour_b.remove(x_an)
#         contour_h.remove(y_an)
#         fin_contourA.append(x_an)
#         fin_contourB.append(y_an)
#         x = x_an
#         y = y_an
#         num += 1

#     # print(fin_contourA)
#     # print(fin_contourB)
#     # plt.plot(fin_contourA,fin_contourB)
#     # plt.show()
#     fin_contourA = [0] + fin_contourA
#     fin_contourB = [0] + fin_contourB
#     return fin_contourA, fin_contourB


# fun(0.25, 1)
# pickle.dump(tck1,open('contourPredict.pkl','wb'))
# loaded_model=pickle.load(open('contourPredict.pkl','rb'))
# inp=[x_input,y_input]
# print(loaded_model.predict([inp]))

# print(contour_b)
# print(contour_h)


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
    # print(np.shape(x_coord))
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
                if math.isnan(y[i]) == False and math.isnan(x[i]) == False:
                    x_coord.append(x[i])
                    y_coord.append(y[i])
                else:
                    print(x[i],y[i])
        # print(np.shape(x), np.shape(y))
    # plt.plot(x_coord,y_coord)
    # plt.show()
    # print(x_coord)
    # x_coord_new = []
    # y_coord_new = []
    
    # for i in range(len(x_coord)):
    #     if math.isnan(y_coord[i]) == False:
    #         x_coord_new.append(x_coord[i])
    #         y_coord_new.append(y_coord[i])
    # print(x_coord_new,y_coord)
    return x_coord,y_coord
    plt.show()