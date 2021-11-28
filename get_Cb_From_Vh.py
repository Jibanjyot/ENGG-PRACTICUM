import pickle
import numpy as np

def fun_cb(x_inp,y_inp):
  contact_angle_predicted = pickle.load(open('predictContactAngle.pkl','rb'))
  volume_predicted = pickle.load(open('predictVolume.pkl','rb'))

  y_new = x_inp

  volume_given = y_inp

  if(int(volume_given)- volume_given == 0):
    rnd = 0
  else:
    rnd = 1


  x_new = np.arange(0,3,0.01)

  min_diff = 99999
  for i in x_new:
    volume_given_result = volume_predicted(i,y_new)[0]
    # print(contact_angle_result)
    if(round(volume_given_result,rnd) == round(volume_given_result,rnd)):
      # print(i)
      diff = abs(volume_given-volume_given_result)
      if(diff<=min_diff):
        min_diff = diff
        b_output = i

  #print(b_output)
  C_output = round(contact_angle_predicted(b_output,y_new)[0],0)
  #print(C_output)
  return b_output,C_output