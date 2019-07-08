import os
from flask_restful import Resource,reqparse
from flask import jsonify

parser = reqparse.RequestParser(trim=True)
parser.add_argument("command")

class RunCom(Resource):
    def post(self):
        args = parser.parse_args()
        comline = args["command"]
        print(comline)
        os.system(comline)
        return jsonify({"success":True})