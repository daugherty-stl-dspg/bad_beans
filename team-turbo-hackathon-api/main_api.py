from flask import Flask, request, Response, send_file
from bson.json_util import dumps, loads
from flask_cors import CORS
from mongo_functions import *
import numpy as np
import cv2
from PIL import Image
from face_recog import matches
import os
import time


app = Flask(__name__)
CORS(app)

# get user by obj_id
@app.route('/test', methods=['GET'])
def test_api():
    data = "Success"
    response = Response(data, status=200, mimetype='application/json')
    return response

# get user by obj_id
@app.route('/users', methods=['GET'])
def get_all_api():
    data = get_all()
    response = Response(data, status=200, mimetype='application/json')
    return response


# get user by obj_id
@app.route('/users/<string:_id>', methods=['GET'])
def getuser_api(_id):
    response_data = get_user(_id)
    if "error" not in response_data:
        response = Response(response_data, status=200, mimetype='application/json')
        return response
    else:
        response = Response("", status=404, mimetype='application/json')
        return response

# insert_user FIX THIS
@app.route("/users", methods=['POST'])
def insert_user_api():
    request_data = request.get_json()
    response_data = insert_user(request_data)
    if 'error' not in response_data:
        response = Response("Insert Success", status=201, mimetype='application/json')
        return response
    else:
        response = Response(dumps(response_data), 200, mimetype='application/json')
        return response

@app.route('/users/<string:_id>', methods=['PUT'])
def update_user_api(_id):
    request_data = request.get_json()
    response_data = update_user(_id, request_data)
    if 'error' not in response_data:
        response = Response(dumps(response_data), status=200, mimetype='application/json')
        return response
    else:
        response = Response(dumps(response_data), 400, mimetype='application/json')
        return response


@app.route('/users/status/<string:_id>', methods=['PUT'])
def update_user_status_api(_id):
    request_data = request.get_json()
    response_data = update_user_status(_id, request_data)
    if 'error' not in response_data:
        response = Response(dumps(response_data), status=200, mimetype='application/json')
        return response
    else:
        response = Response(dumps(response_data), 400, mimetype='application/json')
        return response


# route http posts to this method
@app.route('/api/test', methods=['POST'])
def test():
    r = request
    # convert string of image data to uint8
    nparr = np.fromstring(r.data, np.uint8)
    # decode image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    image = Image.fromarray(img)

    now = time.strftime("%Y%m%d-%H%M%S")

    image.save(r"./temp/monster.jpg")
    monster = matches(r"./temp/monster.jpg")

    if monster == "Unidentified":
        count = get_count()
        monster = "Unidentified" + str(count)
        insert_user({"user_id": monster})

    print(monster)

    image_path = r"monsters/" + monster + now + ".jpg"



    image.save(image_path)

    update_user_status(monster, {"image_location":image_path,
                                 "status": "0",
                                 "lastUpdated": now})

    # do some fancy processing here....

    # build a response dict to send back to client
    response = {'message': 'image received. size={}x{}'.format(img.shape[1], img.shape[0])
                }
    # encode response using jsonpickle
    response_pickled = dumps(response)

    return Response(response=response_pickled, status=200, mimetype="application/json")


@app.route('/image/<string:user_id>', methods=['GET'])
def get_shame_image(user_id):
    file = get_image_location(user_id)
    if file is not None:
        path = os.getcwd()
        filename = os.path.join(path, file)
        # response = Response(os.path.join(path, file), 200, mimetype='application/json')
        return send_file(filename)
    else:
        response = Response("No Image Available", status=200, mimetype='application/json')
        return response


app.run(host='0.0.0.0', port=5000)