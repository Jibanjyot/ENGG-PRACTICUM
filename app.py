from flask import Flask, jsonify, request
from flask_cors import CORS
import pickle
import logging
import os
from werkzeug.utils import secure_filename

from contourPredict import *
from get_bV_From_Ch import *
from get_Cb_From_Vh import *
from get_Ch_From_Vb import *
from get_hV_From_Cb import *
from getVolumeContour import *
from shapeIndexContour import *
from getDropPropertiesFromImage import GetParametersFromImage

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app = Flask(__name__, static_url_path='')
CORS(app)
contactAngle = pickle.load(open('predictContactAngle.pkl', 'rb'))
regimePrediction = pickle.load(open('regimePredict.pkl', 'rb'))
# countourPrediction = pickle.load(open('contourPredict.pkl','rb'))
volumPred = pickle.load(open('predictVolume.pkl', 'rb'))
s_Index = pickle.load(open('predictShapeIndex.pkl', 'rb'))


UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload/image', methods=["POST"])
def GetImageDimensions():
    if 'files' not in request.files:
        resp = jsonify({'message': 'No file part in the request'})
        resp.status_code = 400
        return resp

    files = request.files.getlist('files')

    errors = {}
    success = False

    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'droplet.jpg'))
            success = True
        else:
            errors[file.filename] = 'File type is not allowed'

    # res = GetParametersFromImage()
    # print(res)
    # final = {'cotact_angle_1': res['contactAngle'][0], 'cotact_angle_2': res['contactAngle'][1], 'radius': res['radius'],
    #          'height': res['height'], 'volume': res['volume']}
    # print(final)

    # if success and errors:
    #     errors['message'] = 'File(s) successfully uploaded'
    #     resp = jsonify(errors)
    #     resp.status_code = 500
    #     return resp
    # if success:
    #     resp = jsonify(final)
    #     resp.status_code = 201
    #     return resp
    # else:
    #     resp = jsonify(errors)
    #     resp.status_code = 500
    #     return resp

    if success:
        resp = jsonify({"message": "Uploaded File!"})
        resp.status_code = 201
        return resp

    resp = jsonify({"message": "Something went wrong"})
    resp.status_code = 400
    return resp


@app.route('/process/image', methods=["POST"])
def processImageDimensions():
    # x = request.form.get("res_x")
    # y = request.form.get("res_y")

    res = GetParametersFromImage()
    print(res)
    final = {'cotact_angle_1': res['contactAngle'][0], 'cotact_angle_2': res['contactAngle'][1], 'radius': res['radius'],
             'height': res['height'], 'volume': res['volume']}
    print(final)

    errors = {}
    success = False

    resp = jsonify(final)
    resp.status_code = 200
    return resp


@app.route('/predict/contactAngle', methods=['POST'])
def predict():
    # Set x and y in form value
    x_new = float(request.form.get("x"))
    y_new = float(request.form.get('y'))
    prediction = contactAngle(x_new, y_new)
    return str(round(prediction[0], 0))


@app.route('/predict/shapeIndex', methods=['POST'])
def predictShapeIndex():
    # Set x and y in form value
    x_new = float(request.form.get("x"))
    y_new = float(request.form.get('y'))
    prediction = s_Index(x_new, y_new)
    return str(round(prediction[0][0], 3))


@app.route('/predict/shapeIndexContour', methods=['POST'])
def shapeIndexContourpredict():
    # Set x and y in form value
    x_new = float(request.form.get("x"))
    y_new = float(request.form.get('y'))
    return jsonify(shapeIndex(x_new, y_new))


@app.route('/predict/volumeContour', methods=['POST'])
def volumeContourpredict():
    # Set x and y in form value
    x_new = float(request.form.get("x"))
    y_new = float(request.form.get('y'))
    return jsonify(getVolumeContour(x_new, y_new))


@app.route('/predict/volume', methods=['POST'])
def volumePredict():
    # Set x and y in form value
    x_new = float(request.form.get("x"))
    y_new = float(request.form.get("y"))
    prediction = volumPred(x_new, y_new)
    return str(round(prediction[0], 2))


@app.route('/predict/regime', methods=['POST'])
def regimePredict():
    # Set x and y in form value
    b_input = float(request.form.get("b_input"))
    h_input = float(request.form.get("h_input"))
    x_in = [h_input, b_input]
    prediction = regimePrediction.predict([x_in])
    print(prediction[0])
    return str(prediction[0])


@app.route('/predict/contour', methods=['POST'])
def contourPredict():
    x_input = float(request.form.get("x_input"))
    y_input = float(request.form.get("y_input"))
    inp = [x_input, y_input]
    return jsonify(fun(x_input, y_input))


@app.route('/predict/bv', methods=['POST'])
def predict_bv():
    print(request.form.get("x_input"))
    x_input = float(request.form.get("x_input"))  # contact angle
    y_input = float(request.form.get("y_input"))  # h
    inp = [x_input, y_input]
    return jsonify(fun_bv(x_input, y_input))


@app.route('/predict/cb', methods=['POST'])
def predict_cb():
    print(request.form.get("x_input"))
    x_input = float(request.form.get("x_input"))  # h
    y_input = float(request.form.get("y_input"))  # v
    inp = [x_input, y_input]
    return jsonify(fun_cb(x_input, y_input))


@app.route('/predict/ch', methods=['POST'])
def predict_ch():
    x_input = float(request.form.get("x_input"))  # b
    y_input = float(request.form.get("y_input"))  # v
    inp = [x_input, y_input]
    return jsonify(fun_ch(x_input, y_input))


@app.route('/predict/hv', methods=['POST'])
def predict_hv():
    x_input = float(request.form.get("x_input"))  # b
    y_input = float(request.form.get("y_input"))  # c
    inp = [x_input, y_input]
    return jsonify(fun_hv(x_input, y_input))


@app.route('/test', methods=['GET'])
def test():
    return jsonify({"hello": "IM BCal"})


@app.route('/plotly', methods=['GET'])
def plotly():
    return app.send_static_file('plotly.html')


if __name__ == "__main__":
    app.run(debug=True)
