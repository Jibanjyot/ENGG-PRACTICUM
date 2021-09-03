from flask import Flask,jsonify,request
import pickle
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
contactAngle = pickle.load(open('predictContactAngle.pkl', 'rb'))

@app.route('/predict/contactAngle',methods=['POST'])
def predict():
    #Set x and y in form value
    x_new=float(request.form.get("x"))
    y_new=float(request.form.get('y'))
    prediction = contactAngle(x_new,y_new)
    return jsonify(prediction[0])

if __name__ == "__main__":
    app.run(debug=True)