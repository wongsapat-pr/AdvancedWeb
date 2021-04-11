import pymongo
from bson import json_util
from flask import Flask, jsonify, request

app = Flask(__name__)

myclient = pymongo.MongoClient(
    "mongodb://admin:KAXiti79146@node9150-advweb-12.app.ruk-com.cloud:11120"
)  # เชื่อม DB
# myclient = pymongo.MongoClient("mongodb://admin:KAXiti79146@10.100.2.127")
mydb = myclient["store"]
pro = mydb["product"]
cat = mydb["category"]


# Get All Product
@app.route("/product", methods=["GET"])
# def get_products():
#     products = []
#     for x in pro.find():
#         products.append({"_id":x["_id"],"name":x["name"],"price":x["price"]})
#     return jsonify(products)
def get_products():
    pipel = pro.aggregate(
        [
            {
                "$lookup": {
                    "from": "category",
                    "localField": "cat_id",
                    "foreignField": "_id",
                    "as": "category",
                }
            },
            # {"$unwind": "$category"},
            # {
            #     "$project": {
            #         "_id": 1,
            #         "name": 1,
            #         "price": 1,
            #         "category_name": "$category.name",
            #     }
            # },
        ]
    )
    return json_util.dumps(pipel)


# Get Single Product
@app.route("/product/<name>", methods=["GET"])
# def get_product(name):
#     product = []
#     for x in pro.find({"name":name}):
#         product.append({"_id":str(x["_id"]),"name":x["name"],"price":x["price"]})
#     return jsonify(product)
def get_product(name):
    pipel = pro.aggregate(
        [
            {
                "$lookup": {
                    "from": "category",
                    "localField": "cat_id",
                    "foreignField": "_id",
                    "as": "category",
                }
            },
            {"$unwind": "$category"},
            {
                "$project": {
                    "_id": 1,
                    "name": 1,
                    "price": 1,
                    "category_name": "$category.name",
                }
            },
            {"$match": {"name": name}},
        ]
    )
    return json_util.dumps(pipel)


# Create Product
@app.route("/product", methods=["POST"])
def add_product():
    new_product = {"name": request.json["name"], "price": request.json["price"]}
    x = pro.insert_one(new_product)
    return jsonify({"status": "Create Success"})


# Update Product
@app.route("/product/<name>", methods=["PUT"])
def update_product(name):
    product = {"name": name}
    newdata = {"$set": {"name": request.json["name"], "price": request.json["price"]}}
    x = pro.update_one(product, newdata)

    return jsonify({"status": "Update Success"})


# Delete Product
@app.route("/product/<name>", methods=["DELETE"])
def delete_product(name):
    product = {"name": name}
    x = pro.delete_one(product)
    return jsonify({"status": "Delete success"})


# Web Root Hello
@app.route("/", methods=["GET"])
def get():
    return jsonify({"ms": "Hello Mongo"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
