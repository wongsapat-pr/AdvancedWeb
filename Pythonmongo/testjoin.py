import pymongo 
from bson import json_util
from flask import Flask,jsonify,request
app = Flask(__name__)

myclient = pymongo.MongoClient("mongodb://admin:KAXiti79146@node9150-advweb-12.app.ruk-com.cloud:11120")
mydb = myclient["store"]  
pro = mydb["product"]

# Web Root Hello
@app.route('/', methods=['GET'])
def get():
    return jsonify({'ms': 'Hello Mongo Test'})

@app.route('/test', methods=['GET'])
def get_proall():
    pipel = pro.aggregate(
        [
            {
                "$lookup":
                {
                    "from": "category",
                    "localField": "cat_id",
                    "foreignField": "_id",
                    "as": "category"
                }
            },
            {
                "$unwind":"$category"
            },
            {
                "$project":
                {
                    "_id":1,
                    "name":1,
                    "price":1,
                    "category_name":"$category.name"
                }
            }
        ]
    )
    return json_util.dumps(pipel)

@app.route('/test/<name>', methods=['GET'])
def get_proone(name):
    pipel = pro.aggregate(
        [
            {
                "$lookup":
                {
                    "from": "category",
                    "localField": "cat_id",
                    "foreignField": "_id",
                    "as": "category"
                }
            },
            {
                "$unwind":"$category"
            },
            {
                "$project":
                {
                    "_id":1,
                    "name":1,
                    "price":1,
                    "category_name":"$category.name"
                }
            },
            { "$match" : { "name" : name } }
        ]
    )
    return json_util.dumps(pipel)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)