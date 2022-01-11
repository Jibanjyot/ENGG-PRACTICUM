import pandas as pd
import numpy as np
from scipy import interpolate
import pickle

df_h = pd.read_csv("BohDataN.csv",header=None)
df_b = pd.read_csv("BorDataN.csv",header=None)
df_s = pd.read_csv("ShapeIndexDataN.csv",header=None)

for i in range(0,324):
  df_h[i] = df_h[i].fillna(99999)
  df_b[i] = df_b[i].fillna(99999)
  df_s[i] = df_s[i].fillna(99999)

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
      y1.append(df_s.iloc[i,j])

#x2 ia hstar
#x1 is b star
x = np.array(x1)
y = np.array(x2)
xg, yg = np.meshgrid(x, y,indexing='ij', sparse=True)
z = np.array(y1)
shapeIndex = interpolate.SmoothBivariateSpline(x, y, z,kx=4, ky=5, s=None, eps=1e-16)
# shapeIndex = interpolate.interp2d(x, y, z, kind='quintic')
x_new= 1.5758
y_new = 1.7453

znew = shapeIndex(x_new,y_new)
pickle.dump(shapeIndex,open('predictShapeIndex.pkl','wb'))
loaded_model=pickle.load(open('predictShapeIndex.pkl','rb'))
result=loaded_model(x_new,y_new)
print(result[0])