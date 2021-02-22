import pymongo
from flask import Flask,jsonify,request

app = Flask(__name__)

# myclient = pymongo.MongoClient("mongodb://admin:KAXiti79146@node9150-advweb-12.app.ruk-com.cloud:11120") #เชื่อม DB
myclient = pymongo.MongoClient("mongodb://admin:KAXiti79146@10.100.2.127")
mydb = myclient["store"]  
mycol = mydb["product"]

# Get All Product
@app.route('/product', methods=['GET'])
def get_products():
    products = []
    for x in mycol.find():
        products.append({"_id":str(x["_id"]),"Name":x["Name"],"Price":x["Price"]})
    return jsonify(products)

# Get Single Product
@app.route('/product/<name>', methods=['GET'])
def get_product(name):
    product = []
    for x in mycol.find({"Name":name}):
        product.append({"_id":str(x["_id"]),"Name":x["Name"],"Price":x["Price"]})
    return jsonify(product)

# Create Product
@app.route('/product', methods=['POST'])
def add_product():
    new_product = {"Name":request.json['Name'],"Price":request.json['Price']}
    x = mycol.insert_one(new_product)
    return jsonify({"status":"Create Success"})

# Update Product
@app.route('/product/<name>', methods=['PUT'])
def update_product(name):
    product = {"Name" : name}
    newdata = {"$set":{"Price": request.json["Price"]}}
    x = mycol.update_one(product,newdata)

    return jsonify({"status":"Update Success"})

# Delete Product
@app.route('/product/<name>', methods=['DELETE'])
def delete_product(name):
    product = {"Name" : name}
    x = mycol.delete_one(product)
    return jsonify({"status":"Delete success"})

# Web Root Hello
@app.route('/', methods=['GET'])
def get():
    return jsonify({'ms': 'Hello Mongo'})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
