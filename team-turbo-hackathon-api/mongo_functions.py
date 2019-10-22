from pymongo import MongoClient
from db_config import PW
from bson.json_util import dumps, ObjectId, loads


client = MongoClient('mongodb+srv://Dev_Test:' + PW + '@teamvalour-kdh2f.mongodb.net/test?retryWrites=true')
db = client.coffee_shame

test_obj = {'user_id': 'matt_m',
            'name': 'Matt_McGuirk'}

test_obj2 = {'user_id': 'matt_k',
            'name': 'Matt_Koch'}

def get_user(_id):
    data = db.users.find_one({'user_id': _id})
    if data is not None:
        return dumps(data)
    else:
        try:
            data2 = db.users.find_one({'_id': ObjectId(_id)})
            if data2 is not None:
                return dumps(data2)
        except:
            error_message = {"error": "User not found.",
                             "help_message": "No record for submitted user."}
            return dumps(error_message)


# def insert_user(item):
#     data = db.users.find_one({'user_id': item['user_id']})
#     if data is None:
#         db.users.insert_one(item)
#         return db.users.find({'user_id': item['user_id']}).limit(1)
#     else:
#         errormessage = {"error": "User exists",
#                         "help_message": "User already in system."}
#         return errormessage

def insert_user(item):

    db.users.insert_one(item)
    return db.users.find({'user_id': item['user_id']}).limit(1)



# get all users
def get_all():
    data = dumps(db.users.find())
    return data


# update_doc(doc)
def update_user(user_id, item):
    data = db.users.find_one({'user_id': user_id})
    if data is not None:
        db.users.update({'user_id': user_id}, {"$set": item})
        response_message = {"user_id": user_id,
                           "updated_status": "updated"}
        return response_message
    else:
        error_message = {"error": "User not found",
                        "help_message": "No record for submitted user"}
        return error_message




# update_doc(doc)
def update_user_status(user_id, item):
    data = db.users.find_one({'user_id': user_id})
    if data is not None:
        db.users.update({'user_id': user_id}, {"$set": item})

        response_message = {"user_id": user_id,
                           "updated_status": "updated"}
        return response_message
    else:
        error_message = {"error": "User not found",
                        "help_message": "No record for submitted user"}
        return error_message


# update_doc(doc)
def update_user_image(user_id, filename):
    data = db.users.find_one({'user_id': user_id})
    if data is not None:
        db.users.update({'user_id': user_id}, {"$set": {"image_location":filename}})
        response_message = {"user_id": user_id,
                           "updated_status": "updated"}
        return response_message
    else:
        error_message = {"error": "User not found",
                        "help_message": "No record for submitted user"}
        return error_message


def get_image_location(user_id):
    data = db.users.find_one({'user_id': user_id})
    if data is not None:
        try:
            data = data['image_location']
            return data
        except:
            return None
    else:
        error_message = {"error": "User not found.",
                         "help_message": "No record for submitted user."}
        return dumps(error_message)


def get_count():
    count = db.users.count()
    return count
