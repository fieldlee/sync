import os
from flask_restful import Resource,reqparse
from flask import jsonify
from . import CertPath

parser = reqparse.RequestParser(trim=True)
parser.add_argument("id")
parser.add_argument("sdk")
parser.add_argument("cc")
parser.add_argument("ccname")
class Clone(Resource):
    def post(self):
        args = parser.parse_args()
        id = args["id"]
        sdk = args["sdk"]
        cc = args["cc"]
        ccname = args["ccname"]

        commandline = 'cd /var; git clone %s sdk;'%(sdk)

        if os.path.exists(os.path.join('/var','sdk')):
            commandline = 'cd /var/sdk; git pull;'

        os.popen(commandline)

        projectPath = os.path.join(CertPath,id)

        ccPath = os.path.join(projectPath,'cc')
        if not os.path.exists(ccPath):
            os.mkdir(ccPath,mode=0o777)

        srcPath = os.path.join(ccPath,'src')
        if not os.path.exists(srcPath):
            os.mkdir(srcPath,mode=0o777)


        cccommandline = 'cd %s;git clone %s %s'%(srcPath,cc,ccname)

        if os.path.exists(os.path.join(srcPath,ccname)):
            cccommandline = 'cd %s;git pull;'%(os.path.join(srcPath,ccname))

        os.system(cccommandline)

        return jsonify({"success":True})