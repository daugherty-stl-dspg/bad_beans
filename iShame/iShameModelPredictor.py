import os 
import numpy as np
import cv2
import argparse
from flask import Flask, request, jsonify
import logging
logging.basicConfig(
    format='%(asctime)s.%(msecs)06d %(levelname)-6s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

from keras.models import Model

import build_ishame_model
import preprocess_images

class iShameModelConfig():
    iShameModel = None
    model_config_path = None
    model_weights_path = None
    output_classes = None
    is_regression = False

model_config = iShameModelConfig()

app = Flask(__name__)

def load_ishame_model(input_shape):
    model_config.iShameModel = build_ishame_model.load_model_with_weights(model_config.model_config_path, model_config.model_weights_path, input_shape, model_config.output_classes)
    build_ishame_model.compile_model(model_config.iShameModel, model_config.is_regression)

def load_image(image_path):
    return cv2.imread(image_path)

def process_images(image_list):

    # load each image in list from file
    images = map(load_image, image_list)

    # preprocess each image in list 
    images = map(preprocess_images.preprocess_image, images)

    # combine images in to single array
    image_data = preprocess_images.create_image_data(images)

    return image_data

@app.route("/predict", methods=['POST'])
def predict():

    image_list = request.json["image_paths"]
    image_data = process_images(image_list)

    if(model_config.iShameModel is None):
        load_ishame_model(image_data.shape[1:])

    predictions = model_config.iShameModel.predict(image_data)

    response = {}
    response["predictions"] = []

    for idx, prediction in enumerate(predictions):

        response_item = {}
        response_item["image_path"] = image_list[idx]

        if(not model_config.is_regression):
            response_item["predicted_class"] = int(np.argmax(predictions[idx]))

        response_item["prediction"] = prediction.tolist()

        response["predictions"].append(response_item)

    return response

def set_model_params(args):

    model_config.model_config_path = args['model_config']
    model_config.model_weights_path = args['model_weights']

    if args['output_classes']:
        model_config.output_classes = int(args['output_classes'])
    else:
        model_config.is_regression = True

if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO)

    ap = argparse.ArgumentParser()
    ap.add_argument("-c", "--model-config", required=True,
                    help="filepath to trained model configuration (JSON)")
    ap.add_argument("-w", "--model-weights", required=True,
                    help="filepath to saved model weights")
    ap.add_argument("-o", "--output-classes", required=False,
                    help="number of output classes for model. If not included, assumed to be regression model [range 0.0-1.0]")

    args = vars(ap.parse_args())

    set_model_params(args)

    # Had to turn off threading due to TensorFlow / keras issue with Flask
    # See https://stackoverflow.com/questions/58015489/flask-and-keras-model-error-thread-local-object-has-no-attribute-value
    app.run(debug=False, threaded=False)
