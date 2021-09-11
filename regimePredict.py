import pandas as pd
import numpy as np
from sklearn import neighbors, datasets
import pickle

x1_bowl = []#h values
x2_bowl = []#corresponding b values
y1_bowl = []#corresponding region
df_h_bowl = pd.read_csv("BohDataBowl.csv",header=None)
df_b_bowl = pd.read_csv("BorDataBowl.csv",header=None)

#remove all nan values
for i in range(0,324):
  df_h_bowl[i] = df_h_bowl[i].fillna(99999)
  df_b_bowl[i] = df_b_bowl[i].fillna(99999)
  
x1_bowl = []#h values
x2_bowl = []#corresponding b values
y1_bowl = []#corresponding region
for i in range(0,150):
  for j in range(0,324):
    if(df_h_bowl.iloc[i,j]==99999):
      continue
    else:
      x1_bowl.append(df_h_bowl.iloc[i,j])
      x2_bowl.append(df_b_bowl.iloc[i,j])
      y1_bowl.append(10)#10=bowl
 
x1_Bell = []#h values
x2_Bell = []#corresponding b values
y1_Bell = []#corresponding region
df_h_Bell = pd.read_csv("BohDataBell.csv",header=None)
df_b_Bell = pd.read_csv("BorDataBell.csv",header=None)

#remove all nan values
for i in range(0,324):
  df_h_Bell[i] = df_h_Bell[i].fillna(99999)
  df_b_Bell[i] = df_b_Bell[i].fillna(99999)
  
x1_Bell = []#h values
x2_Bell = []#corresponding b values
y1_Bell = []#corresponding region
for i in range(0,150):
  for j in range(0,324):
    if(df_h_Bell.iloc[i,j]==99999):
      continue
    else:
      x1_Bell.append(df_h_Bell.iloc[i,j])
      x2_Bell.append(df_b_Bell.iloc[i,j])
      y1_Bell.append(11)# 11 bell

x1_balloon = []#h values
x2_balloon = []#corresponding b values
y1_balloon = []#corresponding region
df_h_balloon = pd.read_csv("BohDataBalloon.csv",header=None)
df_b_balloon = pd.read_csv("BorDataBalloon.csv",header=None)

#remove all nan values
for i in range(0,324):
  df_h_balloon[i] = df_h_balloon[i].fillna(99999)
  df_b_balloon[i] = df_b_balloon[i].fillna(99999)
  
x1_balloon = []#h values
x2_balloon = []#corresponding b values
y1_balloon = []#corresponding region
for i in range(0,150):
  for j in range(0,324):
    if(df_h_balloon.iloc[i,j]==99999):
      continue
    else:
      x1_balloon.append(df_h_balloon.iloc[i,j])
      x2_balloon.append(df_b_balloon.iloc[i,j])
      y1_balloon.append(12)#12 balloon

x1_Bulb = []#h values
x2_Bulb = []#corresponding b values
y1_Bulb = []#corresponding region
df_h_Bulb = pd.read_csv("BohDataBulb.csv",header=None)
df_b_Bulb = pd.read_csv("BorDataBulb.csv",header=None)

#remove all nan values
for i in range(0,324):
  df_h_Bulb[i] = df_h_Bulb[i].fillna(99999)
  df_b_Bulb[i] = df_b_Bulb[i].fillna(99999)
  
x1_Bulb = []#h values
x2_Bulb = []#corresponding b values
y1_Bulb = []#corresponding region
for i in range(0,150):
  for j in range(0,324):
    if(df_h_Bulb.iloc[i,j]==99999):
      continue
    else:
      x1_Bulb.append(df_h_Bulb.iloc[i,j])
      x2_Bulb.append(df_b_Bulb.iloc[i,j])
      y1_Bulb.append(13)# 13 bulb
    
x1 = x1_balloon+x1_Bell+x1_bowl+x1_Bulb
x2 = x2_balloon+x2_Bell+x2_bowl+x2_Bulb
y = y1_balloon+y1_Bell+y1_bowl+y1_Bulb

x = []
for i in range(len(x1)):
  x.append([x1[i],x2[i]])



X, y = x, y
knn = neighbors.KNeighborsClassifier(n_neighbors=1)
knn.fit(X, y)
pickle.dump(knn,open('regimePredict.pkl','wb'))
loaded_model=pickle.load(open('regimePredict.pkl','rb'))
b_input = 0.87
h_input = 1.7542
x_in =  [h_input,b_input] #[yvalue,xvalue]
print(loaded_model.predict([x_in]))
if knn.predict([x_in])[0] == 11:
  print("Bell")
if knn.predict([x_in])[0] == 12:
  print("Balloon")
if knn.predict([x_in])[0] == 13:
  print("Bulb")
if knn.predict([x_in])[0] == 10:
  print("Bowl")
  