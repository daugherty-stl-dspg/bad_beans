import os 
import numpy as np
import cv2

from keras.models import load_model
from keras.metrics import MeanSquaredError, CategoricalAccuracy

def load_ishame_model(model_path, metrics):
    return load_model(model_path, custom_objects=metrics)

def load_image(image_path):
    return cv2.imread(image_path)

def preprocess_image(image):
    # assume that initial image is the same size as training data
    # would need to be updated to consolidate with train step so that we have only one pipeline
    scale_factor = 0.5

    image = cv2.resize(image,(int(image.shape[1]*scale_factor), int(image.shape[0]*scale_factor)))

    return image

def predict(model, image):
    result = model.predict(image)
    return result

def main(model_dir, model_name, metrics, image_dir, image_path):
    image_path = os.path.join(image_dir, image_name)
    image = load_image(image_path)
    image = preprocess_image(image)

    model_path = os.path.join(model_dir, model_name)
    model = load_ishame_model(model_path, metrics)


    result = predict(model, image)

    print(result)

if __name__ == "__main__":
    model_dir = '/c/Users/rrr0901/Documents/Workspace/iShame/data/coffee_video/model'
    model_name = 'coffee_class_label_data_v2.model'
    metrics= {
    'valid_accuracy': ValidAccuracy
    }

    image_dir = '/c/Users/rrr0901/Documents/Workspace/iShame/data/coffee_pictures'
    image_name = 'IMG_20200401_083412.jpg'

    main(model_dir, model_name, image_dir, image_name, metrics)