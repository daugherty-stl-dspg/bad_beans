import numpy
import matplotlib
import cv2
import dlib
import face_recognition
from PIL import Image
import pickle
import os


def matches(shame_name):
    with open('names.pkl', 'rb') as f:
        names = pickle.load(f)


    with open('encodings.pkl', 'rb') as f:
        encodings = pickle.load(f)

    shamer = face_recognition.load_image_file(shame_name)
    try:
        shamer = face_recognition.face_encodings(shamer)[0]
    except:
        return "Cannot find Shamer."

    match = face_recognition.compare_faces(encodings, shamer)

    if any(match) != True:
        return "Unidentified"
    else:
        for i in match:
            if i == True:
                return names[match.index(i)]






