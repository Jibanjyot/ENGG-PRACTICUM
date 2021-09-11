import pandas as pd
import numpy as np
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model

df= pd.read_excel("boundaryPoints.xlsx",header=None)

x_points = list(df.iloc[:,0])
y_points = list(df.iloc[:,1])

from scipy import interpolate
x_input = 0.04709
y_input = 0.64205

tck = interpolate.splrep(x_points, y_points)
y_out = interpolate.splev(x_input, tck)
if y_out-y_input < 0:
  print("Unstable region")
  print(y_out,y_input)
else:
  print("stable region")
  print("expected output",y_out)
  print("given output",y_input)