import os
from flask import Flask, jsonify
from flask_restful import Api
from flask_cors import CORS

from resources.risk_type import RiskTypeList
from resources.field import FieldList

from resources.risk_type import RiskTypeDetail
from resources.field import FieldDetail

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', default='sqlite:///db.sqlite3')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'mysecret'
api = Api(app)

# GET
api.add_resource(RiskTypeList, '/v1/risk_types')

# GET
api.add_resource(FieldList, '/v1/fields')

# GET, DELETE
api.add_resource(RiskTypeDetail, '/v1/risk_type/<int:_id>')

# GET, DELETE
api.add_resource(FieldDetail, '/v1/field/<int:_id>')


if __name__ == '__main__':
    from db import db
    db.init_app(app)

    # Create db tables if they don't exist
    @app.before_first_request
    def create_tables():
        db.create_all()

    app.run(debug=True)
