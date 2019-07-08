import os
from flask import request,jsonify
from flask_restful import Resource
from . import untils,CertPath

class UpCertFile(Resource):
    def post(self):
        try:
            file = request.files['file']
        except Exception as e:
            return jsonify({'success': False,'err': str(e)})

        if file and untils.Allowed_file(file.filename):
            filename = file.filename
            certfilePath = os.path.join(CertPath,filename)
            if os.path.exists(certfilePath):
                os.remove(certfilePath)
            file.save(certfilePath)

            if untils.UNzip(CertPath,filename):
                return jsonify({'success': True})
            else:
                return jsonify({'success': False,'err': 'unzip error'})
        else:
            return jsonify({'success': False,'err': 'file error'})