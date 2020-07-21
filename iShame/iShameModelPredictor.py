import os 
import numpy as np
import cv2
import argparse
from flask import Flask
import logging

from keras.models import Model

import build_ishame_model
import preprocess_images

class iShameModelConfig():
    iShameModel = None
    model_config_path = None
    model_weight_path = None
    output_classes = None
    is_regression = False

model_config = iShameModelConfig()

app = Flask(__name__)

def load_ishame_model(input_shape):
    conv_layers, conn_layers = build_ishame_model.load_model_def(model_config.model_config_path)

    model_config.model = build_ishame_model.build_model(input_shape, conv_layers, conn_layers, model_config.output_classes)
    model_config.model.load_weights(model_config.model_weight_path)
    build_ishame_model.compile_model(model_config.iShameModel, model_config.is_regression)

def load_image(image_path):
    return cv2.imread(image_path)

@app.route("/predict")
def predict(image_path):

    image = load_image(image_path)

    image = preprocess_images.preprocess_image(image)

    input_shape = image.shape

    if(model_config.iShameModel is None):
        load_ishame_model(input_shape)

    result = None
    #result = model.predict(image)
    return result

def set_model_params(args):

    model_config.model_config_path = args['model_config']
    model_config.model_weight_path = args['model_weights']

    if args['output_classes']:
        model_config.output_classes = args['output_classes']
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
                    help="number of output classes for model. If not included, assumed to be regression model [range 0-1]")

    args = vars(ap.parse_args())

    set_model_params(args)

    # model_dir = '/c/Users/rrr0901/Documents/Workspace/iShame/data/coffee_video/model'
    # model_name = 'coffee_class_label_data_v2.model'

    # image_dir = '/c/Users/rrr0901/Documents/Workspace/iShame/data/coffee_pictures'
    # image_name = 'IMG_20200401_083412.jpg'

    app.run(debug=True)
