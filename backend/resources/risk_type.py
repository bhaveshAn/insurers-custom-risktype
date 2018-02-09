from flask_restful import Resource, reqparse
from models.risk_type import RiskType
from models.field import Field
from flask import jsonify, request 


class RiskTypeList(Resource):

    def get(self):
        return {'risk_types': [x.json() for x in RiskType.query.all()]}

    def post(self):
        json_data = request.get_json(force=True)

        risk_type_obj = RiskType(
            json_data['name']
        )

        try:
            risk_type_obj.save()
        except Exception as e:
            return {'message': 'An error occurred inserting into db: {}'.format(e)}, 500

        return {'risk_type': risk_type_obj.json()}, 201

class RiskTypeDetail(Resource):

    def get(self, _id):
        risk_type = RiskType.query.filter_by(id=_id).first()
        fields = []
        for field in Field.query.filter_by(risk_type_id=_id):
            field_obj = {}
            field_obj['id'] = field.id
            field_obj['name'] = field.name
            field_obj['type'] = field.type
            fields.append(field_obj)
        response  = {"risk_type": risk_type.json(), 'fields': fields}
        return jsonify(response)
        fields = [y for y in Field.query.filter_by(risk_type_id=_id).all()]
        response  = {"risk_type": risk_type.json(), 'fields': "Hello"}
        return response
        #return {'risk_type': RiskType.query.filter_by(id=_id)}
        return {'risk_type': risk_type.json(), 'fields': [y.json for y in Field.query.filter_by(risk_type_id=_id)]}

    def delete(self, _id):
        risk_type_obj = RiskType.query.filter_by(id=_id)

        status = 404
        message = 'Risk Type not found'
        if risk_type_obj:
            risk_type_obj.delete()
            status = 200
            message = 'Image deleted'

        return {'message': message}, status
