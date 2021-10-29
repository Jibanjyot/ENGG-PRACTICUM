import pickle
import numpy as np

contact_angle_predicted = pickle.load(open('predictContactAngle.pkl','rb'))
volume_predicted = pickle.load(open('predictVolume.pkl','rb'))

y_new = 1.49

contact_angle_given = 63
if(int(contact_angle_given)-contact_angle_given == 0):
  rnd = 0
else:
  rnd = 1


x_new = np.arange(0,3,0.01)

min_diff = 99999
for i in x_new:
  contact_angle_result = contact_angle_predicted(i,y_new)[0]
  # print(contact_angle_result)
  if(round(contact_angle_result,rnd) == round(contact_angle_given,rnd)):
    # print(i)
    diff = abs(contact_angle_given-contact_angle_result)
    if(diff<=min_diff):
      min_diff = diff
      b_output = i

print(b_output)
V_output = round(volume_predicted(b_output,y_new)[0],3)
print(V_output)