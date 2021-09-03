import pandas as pd
import numpy as np
from scipy.interpolate import RegularGridInterpolator
from scipy import interpolate
import pickle 

df_h = pd.read_csv("BohDataN.csv",header=None)
df_b = pd.read_csv("BorDataN.csv",header=None)
df_c = pd.read_csv("CADataN.csv",header=None)

for i in range(0,324):
  df_h[i] = df_h[i].fillna(99999)
  df_b[i] = df_b[i].fillna(99999)
  df_c[i] = df_c[i].fillna(99999)

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
      y1.append(df_c.iloc[i,j])

x = np.array(x1)
y = np.array(x2)
xg, yg = np.meshgrid(x, y,indexing='ij', sparse=True)
z = np.array(y1)
g = interpolate.interp2d(x, y, z, kind='quintic')

x_new= 1.5758
y_new = 1.7453

znew = g(x_new,y_new)
pickle.dump(g,open('predictContactAngle.pkl','wb'))
loaded_model=pickle.load(open('predictContactAngle.pkl','rb'))
result=loaded_model(x_new,y_new)
print(result[0])