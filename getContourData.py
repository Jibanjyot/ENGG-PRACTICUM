#decide stable or unstable
def contourData(b_star_input,h_star_input,contact_angle_predicted):
  df= pd.read_excel("boundaryPoints.xlsx",header=None)
  x_points = list(df.iloc[:,0])
  y_points = list(df.iloc[:,1])
  tck = interpolate.splrep(x_points, y_points)


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

  #x2 ia hstar
  #x1 is b star
  x = np.array(x1)
  y = np.array(x2)
  xg, yg = np.meshgrid(x, y,indexing='ij', sparse=True)
  z = np.array(y1)
  g = interpolate.interp2d(x, y, z, kind='quintic')



  x_input = b_star_input
  y_input = h_star_input
  y_out = interpolate.splev(x_input, tck)
  if y_out-y_input < 0:
    print("Unstable region")
    #print(y_out,y_input)
  elif (x_input<0 and y_input>0) or (x_input<0 and y_input< 0) or (x_input>0 and y_input<0):
    print("Unstable region")
    #print(y_out,y_input)
    

  else:
    print("stable region")
    #print("expected output",y_out)
    #print("given output",y_input)
    contactAngle = g(x_input,y_input)
    warnings.filterwarnings("ignore", category=RuntimeWarning) 
    #we need to output znew[0]
    print(round(contactAngle[0],0))


  b_star_array = np.arange(0,4,0.01)
  h_star_array = np.arange(0,4,0.01)
  # h_input = 1.5
  c_angle_input = round(contactAngle[0],0)
  # print(b_star_array)
  contour_b = []
  contour_h = []

  df= pd.read_csv("boundaryThinFilmData.csv",header=None)
  x_thinFilm = list(df.iloc[1:,0])
  y_thinFilm = list(df.iloc[1:,1])
  tck1 = interpolate.splrep(x_thinFilm, y_thinFilm)
  


  for j in h_star_array:
    for i in b_star_array:
      y_out1 = interpolate.splev(i, tck1)
      if j < y_out1:
        continue
      y_out = interpolate.splev(i, tck)
      if y_out-j < 0:
        continue
      contactangle = round(g(i,j)[0],0)
      if contactangle == c_angle_input:
        contour_b.append(i)
        contour_h.append(j)

  import matplotlib.pyplot as plt
  
  # print(contour_h)
  # print(contour_b,contour_h)
  plt.scatter(contour_b,contour_h)
  plt.show
  return contour_b,contour_h
  # plt.scatter(contour_b,contour_h)

contour_b, contour_h = contourData(1.5,1.5,60)