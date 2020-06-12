import cv2
import numpy as np
import face_recognition
import glob

#use face_recognition package to encode photographs
def faceencoding(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    boxes = face_recognition.face_locations(img)
    encodings = face_recognition.face_encodings(img,boxes)
        
    area = 0 
    top=right=bottom=left = 0 
    enc = 0
    for i, (t, rt, b, l) in enumerate(boxes):
        box_area = (rt-l)*(b-t)
        if box_area > area:
            top = int(t)
            bottom = int(b)
            right = int(rt)
            left = int(l)
            area = box_area
            enc = encodings[i]
    return (left,top,right,bottom), enc

#measure distance between two encodings using euclidian distance
def euclideandistance(enc1,enc2):
    totalsquareddistance = 0
    
    for i in range(0,128):
        distancesquared = (enc1[i] - enc2[i])**2
        totalsquareddistance = totalsquareddistance + distancesquared
    distance = np.sqrt(totalsquareddistance)
    return(distance)

#encode repository of known users
def encodeknownusers():
    knownusers = []
#need location of known users in S3     
    for filepath in glob.iglob('KnownFaces/*.jpg'):
        knownface = cv2.imread(filepath)
        knownface = cv2.cvtColor(knownface, cv2.COLOR_BGR2RGB)
        knownbox, knownenc = faceencoding(knownface)
        knownusers.append([filepath, knownenc])
    return knownusers

#encode unknown user
def encodeunknownuser():
#need location of incoming photo in S3 
    unknown = cv2.imread('TestFaces/Unknown.jpg')
    unknown = cv2.cvtColor(unknown, cv2.COLOR_BGR2RGB)
    unknownbox, unknownenc = faceencoding(unknown)
    return unknownenc

#compare unknown user to known user to find closest and evaluate for match
def compareunknowntounknown(knownusers, unknownenc):
    matchthreshold = .6
    minimumdistance = 1
    
    for user in knownusers:
        knownenc = user[1]
        distance = euclideandistance(unknownenc, knownenc)
        if distance < minimumdistance:
            culpritname = user[0]#[user[0].find('KnownFaces\\') + len('KnownFaces\\'):user[0].rfind('.jpg')]
            minimumdistance = distance
    if minimumdistance < matchthreshold:
        return(culpritname, minimumdistance)
    else:
        return("No Known User")

#run evaluation functions and return result    
def evaluatephoto():
    knownusers = encodeknownusers()
    unknownuser = encodeunknownuser()
    if isinstance(unknownuser, int) == True:
        results = "No Face Found"
    else:
        results = compareunknowntounknown(knownusers, unknownuser)
#need format of output, currently printing
    print(results)
    
evaluatephoto()