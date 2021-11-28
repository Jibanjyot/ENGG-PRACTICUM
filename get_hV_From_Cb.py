import pickle
import numpy as np

def fun_hv(x_inp,y_inp):
  contact_angle_predicted = pickle.load(open('predictContactAngle.pkl','rb'))
  volume_predicted = pickle.load(open('predictVolume.pkl','rb'))
  x_new = x_inp

  contact_angle_given = y_inp
  y_new = np.arange(0,3,0.01)
  rnd=1
  if int(contact_angle_given)-contact_angle_given==0:
    rnd=0

  min_diff = 99999
  for j in y_new:
    contact_angle_result = contact_angle_predicted(x_new,j)[0]
    # if(round(contact_angle_result,rnd) == round(contact_angle_given,rnd)):
    diff = abs(contact_angle_given-contact_angle_result)
    if(diff<=min_diff):
      min_diff = diff
      h_output = j

  #print(h_output)
  V_output = round(volume_predicted(x_new,h_output)[0],3)
  #print(V_output)
  return h_output,V_output

