import os

ALLOWED_EXTENSIONS = set(['tar','json','tx'])
def Allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def UNzip(path,filename):
     if '.' in filename:
         id = filename.rsplit('.', 1)[0]
         extname = filename.rsplit('.', 1)[1]
         if extname in 'tar':
             if os.path.exists(os.path.join(path,id)) :
                 RemoveFloder(os.path.join(path,id))
             os.system('cd %s ; tar -xvf %s ./'%(path,filename))
             return True
         else:
             return False
     else:
         return False


def RemoveFloder(top):
    for root, dirs, files in os.walk(top, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))

        for name in dirs:
            os.rmdir(os.path.join(root, name))

        os.rmdir(root)