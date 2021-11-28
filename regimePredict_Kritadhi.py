import pandas as pd
import numpy as np
from shapely.geometry import Point, Polygon

def regimePredict(x,y):
  #BALLOON
  df_balloon = pd.read_csv("dataBoundaryBalloon.csv",header=None)

  x_balloon = list(df_balloon.iloc[2:,0].astype(float))
  y_balloon = list(df_balloon.iloc[2:,1].astype(float))

  L_balloon = []
  for i in range(len(x_balloon)):
    L_balloon.append((x_balloon[i],y_balloon[i]))

  p1_balloon = Point(x, y)

  # Create a Polygon
  coords_balloon = L_balloon
  poly_balloon = Polygon(coords_balloon)
  if(p1_balloon.within(poly_balloon) == True):
    print("BALLOON")

  #BULB
  df_bulb = pd.read_csv("dataBoundaryBulb.csv",header=None)

  x_bulb = list(df_bulb.iloc[2:,0].astype(float))
  y_bulb = list(df_bulb.iloc[2:,1].astype(float))

  L_bulb = []
  for i in range(len(x_bulb)):
    L_bulb.append((x_bulb[i],y_bulb[i]))

  p1_bulb = Point(x, y)

  # Create a Polygon
  coords_bulb = L_bulb
  poly_bulb = Polygon(coords_bulb)
  if(p1_bulb.within(poly_bulb) == True):
    print("BULB")

  #BELL
  df_bell = pd.read_csv("dataBoundaryBell.csv",header=None)

  x_bell = list(df_bell.iloc[2:,0].astype(float))
  y_bell = list(df_bell.iloc[2:,1].astype(float))

  L_bell = []
  for i in range(len(x_bell)):
    L_bell.append((x_bell[i],y_bell[i]))

  p1_bell = Point(x, y)

  # Create a Polygon
  coords_bell = L_bell
  poly_bell = Polygon(coords_bell)
  if(p1_bell.within(poly_bell) == True):
    print("BELL")


  #BOWL
  df_bowl= pd.read_excel("bowl.xlsx",header=None)

  x_bowl = list(df_bowl.iloc[2:,0].astype(float))
  y_bowl = list(df_bowl.iloc[2:,1].astype(float))

  L_bowl = []
  for i in range(len(x_bowl)):
    L_bowl.append((x_bowl[i],y_bowl[i]))

  p1_bowl = Point(x, y)


  # Create a Polygon
  coords_bowl = L_bowl
  poly_bowl = Polygon(coords_bowl)
  if(p1_bowl.within(poly_bowl) == True):
    print("BOWL")

regimePredict(0.75,1.5)