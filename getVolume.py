import pandas as pd
import numpy as np
from scipy import interpolate

df_h = pd.read_csv("BohDataN.csv",header=None)
df_b = pd.read_csv("BorDataN.csv",header=None)
df_v = pd.read_csv("VolumeDataN.csv",header=None)

for i in range(0,324):
  df_h[i] = df_h[i].fillna(99999)
  df_b[i] = df_b[i].fillna(99999)
  df_v[i] = df_v[i].fillna(99999)

x1 = []
x2 = []
y1 = []
for i in range(0,150):
  for j in range(0,324):
    if(df_h.iloc[i,j]==99999):
      continue
    else:
      x2.append(df_h.iloc[i,j])
      x1.append(df_b.iloc[i,j])
      y1.append(df_v.iloc[i,j])

#x2 ia hstar
#x1 is b star
x = np.array(x1)
y = np.array(x2)
xg, yg = np.meshgrid(x, y,indexing='ij', sparse=True)
z = np.array(y1)
g = interpolate.interp2d(x, y, z, kind='quintic')


x_new= 1.5758
y_new = 1.7453

znew = g(x_new,y_new)