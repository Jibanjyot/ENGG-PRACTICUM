from flask import Flask,jsonify,request
import pickle
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
contactAngle = pickle.load(open('predictContactAngle.pkl', 'rb'))
regimePrediction=pickle.load(open('regimePredict.pkl','rb'))

@app.route('/predict/contactAngle',methods=['POST'])
def predict():
    #Set x and y in form value
    x_new=float(request.form.get("x"))
    y_new=float(request.form.get('y'))
    prediction = contactAngle(x_new,y_new)
    return jsonify(prediction[0])

@app.route('/predict/regime',methods=['POST'])
def regimePredict():
    #Set x and y in form value
    b_input=float(request.form.get("b_input"))
    h_input=float(request.form.get("h_input"))
    x_in=[h_input,b_input]
    prediction = regimePrediction.predict([x_in])
    print(prediction[0])
    return str(prediction[0]) 

if __name__ == "__main__":
    app.run(debug=True)