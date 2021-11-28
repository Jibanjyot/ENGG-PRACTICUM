import pickle
import numpy as np

def fun_ch(x_inp,y_inp):
  contact_angle_predicted = pickle.load(open('predictContactAngle.pkl','rb'))
  volume_predicted = pickle.load(open('predictVolume.pkl','rb'))

  x_new = x_inp

  volume_given = y_inp

  if(int(volume_given)- volume_given == 0):
    rnd = 0
  else:
    rnd = 1


  y_new = np.arange(0,3,0.01)

  min_diff = 99999
  for j in y_new:
    volume_given_result = volume_predicted(x_new,j)[0]
    # print(contact_angle_result)
    # if(round(volume_given_result,rnd) == round(volume_given_result,rnd)):
      # print(i)
    diff = abs(volume_given-volume_given_result)
    if(diff<=min_diff):
      min_diff = diff
      h_output = j

  #print(h_output)
  C_output = round(contact_angle_predicted(x_new,h_output)[0],3)
  #print(C_output)
  return h_output,C_output