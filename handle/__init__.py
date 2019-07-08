import os
CertPath = os.path.join("/var","certification")
SdkPath = os.path.join('/var','sdk')
if not os.path.exists(CertPath):
    os.mkdir(CertPath,mode=0o777)