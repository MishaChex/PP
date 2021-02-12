from flask_restful import Resource

from flask import json, Response, request
from models import *
from werkzeug.security import generate_password_hash, check_password_hash

from sqlalchemy.ext.declarative import DeclarativeMeta

from core import session

class AlchemyEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data)
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            return fields

        return json.JSONEncoder.default(self, obj)

class AddUser(Resource):
    def post(self):
        data = request.json
        try:
            user = User(data["login"], data["password"], data["name"], data["email"], data["phone"])
            user.password = generate_password_hash(data['password'])

            checkuser = session.query(User).filter(User.login == user.login).all()
            if checkuser:
                return Response(
                    response=json.dumps({"message": "user with such login already exist"}),
                    status=409,
                    mimetype="appl ication/json"
                )
            session.add(user)
            session.flush()
            session.commit()
            return Response(
                response=json.dumps({"message": "Success"}),
                status=200,
                mimetype="application/json"
            )
        except:
            return Response(
                response=json.dumps({"message": "Invalid input"}),
                status=405,
                mimetype="application/json"
            )


class GetUser(Resource):
    def get(self, id):
        user = session.query(User).get(id)
        if user:
            return Response(
                response=json.dumps(user, cls=AlchemyEncoder),
                status=201,
                mimetype="application/json"
            )
        return Response(
                response=json.dumps({"message": "Not found"}),
                status=400,
                mimetype="application/json"
            )


class UpdateUser(Resource):
    def put(self, id):
        data = request.json
        try:
            user = session.query(User).get(id)
            if not user:
                return Response(
                    response=json.dumps({"message": "invalid id"}),
                    status=400,
                    mimetype="application/json"
                )
            if "login" in data:
                user.login = data["login"]
            if "password" in data:
                user.password = generate_password_hash(data['password'])
            if "name" in data:
                user.name = data["name"]
            if "email" in data:
                user.email = data["email"]
            if "phone" in data:
                user.phone_number = data["phone"]
            session.commit()
            return Response(
                response=json.dumps({"message": "Success"}),
                status=200,
                mimetype="application/json"
            )
        except Exception as e:
            return Response(
                response=json.dumps({"message": "Invalid input"}),
                status=405,
                mimetype="application/json"
            )
class AddPharmacy(Resource):
    def post(self):
        data = request.json
        try:
            bank = Pharmacy(data["name"], data["phone"], data["branch"], data["email"], data["address"])
            session.add(bank)
            session.commit()
            return Response(
                response=json.dumps({"message": "Success"}),
                status=200,
                mimetype="application/json"
            )
        except:
            return Response(
                response=json.dumps({"message": "Invalid input"}),
                status=405,
                mimetype="application/json"
            )


class GetPharmacy(Resource):
    def get(self, id):
        bank = session.query(Pharmacy).get(id)
        if bank:
            return Response(
                response=json.dumps(bank, cls=AlchemyEncoder),
                status=201,
                mimetype="application/json"
            )
        return Response(
                response=json.dumps({"message": "Not found"}),
                status=400,
                mimetype="application/json"
            )


class AddMedicine(Resource):
    def post(self,pharmacy_id):
        data = request.json
        try:
            medicine = Medicine(data["name"], data["description"], data["category"], pharmacy_id)
            session.add(medicine)
            session.commit()
            return Response(
                response=json.dumps({"message": "Success"}),
                status=200,
                mimetype="application/json"
            )
        except:
            return Response(
                response=json.dumps({"message": "Invalid input"}),
                status=405,
                mimetype="application/json"
            )


class GetMedicine(Resource):
    def get(self, medicine_id):
        medicine = session.query(Medicine).get(medicine_id)
        if medicine:
            return Response(
                response=json.dumps(medicine, cls=AlchemyEncoder),
                status=201,
                mimetype="application/json"
            )
        return Response(
                response=json.dumps({"message": "Not found"}),
                status=400,
                mimetype="application/json"
            )

