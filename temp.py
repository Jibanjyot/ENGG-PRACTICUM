import pickle
import numpy as np
from numpy.lib.index_tricks import s_
shapeIndex=pickle.load(open('predictShapeIndex.pkl','rb'))
prediction = shapeIndex(2, 1)
print(str(round(prediction[0],3)))