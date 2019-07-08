from flask_restful import Resource
from flask import request,jsonify
import os
from . import untils,SdkPath

class UpConfigFile(Resource):
    def post(self):
        try:
            file = request.files['file']
        except Exception as e:
            return jsonify({'success': False,'err': str(e)})

        if file and untils.Allowed_file(file.filename):
            filename = file.filename
            sdkfile = os.path.join(SdkPath,filename)
            file.save(sdkfile)
            return jsonify({'success': True})
        else:
            return jsonify({'success': False,'err': 'file error'})