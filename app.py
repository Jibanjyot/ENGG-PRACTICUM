from flask import Flask, jsonify, request
from flask_cors import CORS
import pickle
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app = Flask(__name__, static_url_path='')
CORS(app)
contactAngle = pickle.load(open('predictContactAngle.pkl', 'rb'))


@app.route('/predict/contactAngle', methods=['POST'])
def predict():
    # Set x and y in form value
    x_new = float(request.form.get("x"))
    y_new = float(request.form.get('y'))
    prediction = contactAngle(x_new, y_new)
    return jsonify(prediction[0])


@app.route('/test', methods=['GET'])
def test():
    return jsonify({"hello": "IM BCal"})


@app.route('/plotly', methods=['GET'])
def plotly():
    return app.send_static_file('plotly.html')


if __name__ == "__main__":
    app.run(debug=True)
