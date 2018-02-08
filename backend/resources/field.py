from flask_restful import Resource, reqparse
from flask import jsonify, request
from models.field import Field
from models.risk_type import RiskType


class FieldList(Resource):

    def get(self):
        return {'fields': [x.json() for x in Field.query.all()]}

    def post(self):
        json_data = request.get_json(force=True)
        risk_type = RiskType.query.filter_by(name=json_data['risk_type_name']).first()
        risk_type_id = risk_type.id
        

        field_obj = Field(
            json_data['name'],
            json_data['type'],
            json_data['value'],
            risk_type_id
        )

        try:
            field_obj.save()
        except Exception as e:
            return {'message': 'An error occurred inserting into db: {}'.format(e)}, 500

        return field_obj.json(), 200


class FieldDetail(Resource):

    def get(self, _id):
        field_obj = Field.query.filter_by(id=_id).first()

        if not field_obj:
            return {'message': 'Field not found'}, 404

        return {'field': field_obj.json()}, 200


    def delete(self, _id):
        field_obj = Field.query.filter_by(id=_id)

        status = 404
        message = 'Field not found.'
        if field_obj:
            status = 200
            message = 'Field deleted'
            field_obj.delete()

        return {'message': message}, status
