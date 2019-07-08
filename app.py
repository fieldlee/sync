from flask import Flask
from flask_restful import Api
from handle import CertPath,certfile,configfile,runCom,txfile,clone

baasApp = Flask(__name__)
baasApp.config['MAX_CONTENT_LENGTH'] = 60 * 1024 * 1024
baasApp.config['UPLOAD_PATH'] = CertPath
api = Api(baasApp)

api.add_resource(certfile.UpCertFile,'/upcert')

api.add_resource(txfile.UpTxFile,'/uptx')

api.add_resource(configfile.UpConfigFile,'/upconfig')

api.add_resource(runCom.RunCom,'/runcom')

api.add_resource(clone.Clone,'/clone')

if __name__ == "__main__":
    baasApp.run(debug=True,port=8000)