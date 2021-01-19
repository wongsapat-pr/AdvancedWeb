from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

#Init app
app = Flask(__name__)

#Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://webadmin:FFGqce84823@node8579-advweb-12.app.ruk-com.cloud:11102/CloudDB'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
#Init db
db = SQLAlchemy(app)
#Init ma
ma = Marshmallow(app)

#Staff Class/Model
class Staffs(db.Model):
    id = db.Column(db.String(13), primary_key=True, unique=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(25))
    phone = db.Column(db.String(10))
    
    def __init__(self, id, name, email, phone):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone

# Staff Schema
class StaffSchema(ma.Schema):
    class Meta:
        fields =('id', 'name', 'email', 'phone')

# Init Schema 
staff_schema = StaffSchema()
staffs_schema = StaffSchema(many=True)

# Get All Staffs
@app.route('/staffs', methods=['GET'])
def get_staffs():
    all_staffs = Staffs.query.all()
    result = staffs_schema.dump(all_staffs)
    return jsonify(result)

# Web Root Hello
@app.route('/', methods=['GET'])
def get():
    return jsonify({'ms': 'Hello Cloud DB'})

# Run Server
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)