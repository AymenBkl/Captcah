import flask
import io
from flask import Flask, jsonify, request 
from detect import *

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def infer_image():
    # Catch the image file from a POST request
    image_base = request.get_json()["image"]
    
    # Return on a JSON format
    return jsonify(prediction=Captcha_detection(image_base))
    

@app.route('/', methods=['GET'])
def index():
    return 'captcha detection'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')