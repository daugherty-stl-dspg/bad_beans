import cv2
import logging
import time
import requests
import base64
import json
import os

# train with openCV haarcascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# create video capture object using lappy cam
cap = cv2.VideoCapture(0)

while True:
    # output images
    ret, img = cap.read()
    
    # convert to greyscale
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # deetect the faces
    faces = face_cascade.detectMultiScale(grey, 1.1, 4)
    
    # draw rectangle on the facesx
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0, 0, 255), 2)
    
    # display rectangles
    cv2.imshow('img', img)
    
    # break if esc key hit
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    
    if k==120: # number for x

        # Log that someone has been detected as not filling up the coffee
        logging.warning('Scumbag Detected')

        # set now as the name of the file with a time and date stamp
        image_file = 'temp.jpg'

        # write the image with the name created
        cv2.imwrite(image_file, img)
        
        try:
            url = 'https://df27kfwowd.execute-api.us-east-2.amazonaws.com/DEV/upload-on-s3'

            with open(image_file, 'rb') as data:
                b64_image = base64.b64encode(data.read())
                requests.post(url, data=b64_image)
            
            os.remove(image_file)

        except Exception as e:
            logging.error(e)

# Turn off camera
cap.release()

# Get rid of window
cv2.destroyAllWindows()