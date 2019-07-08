from flask_restful import Resource,reqparse
from flask import request,jsonify
import os
from . import untils,CertPath

parser = reqparse.RequestParser(trim=True)
parser.add_argument("id")

class UpTxFile(Resource):
    def post(self):
        args = parser.parse_args()
        id = args["id"]

        try:
            file = request.files['file']
        except Exception as e:
            return jsonify({'success': False,'err': str(e)})

        if file and untils.Allowed_file(file.filename):

            filename = file.filename
            txPath = os.path.join(CertPath,id,filename)
            file.save(txPath)

            return jsonify({'success': True})
        else:
            return jsonify({'success': False,'err': 'file error'})