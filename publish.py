## =================================================================== ##
#  this is file test.py, created at 27-Apr-2014                #
#  maintained by Gustavo Rabello dos Anjos                              #
#  e-mail: gustavo.rabello@gmail.com                                    #
## =================================================================== ##


import paramiko,os,shutil
from subprocess import call
from stat import S_ISDIR

server ='www.unidades.uerj.br'
username = 'gesar'
password = 'abj4g79@zq'
port = 22

transport = paramiko.Transport((server, port))
transport.connect(username=username, password=password)
sftp = paramiko.SFTPClient.from_transport(transport)

def isdir(path):
 try:
  return S_ISDIR(sftp.stat(path).st_mode)
 except IOError:
  return False

def rm(path):
 files = sftp.listdir(path=path)
 while files != 0:

  if not path.endswith("/"):
   path = "%s/" % path
 
  # remove dir if files is empty
  if not len(files):
   if path == '/paginas/':
    break
   sftp.rmdir(path)
   return
 
  for f in files:
   filepath = "%s/%s" % (path, f)
   if isdir(filepath):
    rm(filepath)
   else:
    sftp.remove(filepath)

  files = sftp.listdir(path=path)

def genSite():
 # removing local directory paginas
 directory = './paginas'
 if os.path.exists(directory):
  shutil.rmtree(directory)

 # generating webpage into paginas folder
 call(['hyde','gen'])


def upload(source,destination):
 sftp.put(source,destination)


if __name__ == "__main__":
 path='/paginas'

 print ""
 print "---> removing server web site..."
 rm(path)
 print "---> generation local web site..."
 genSite()
 #print "---> uploading web site from local to server..."
 #upload('.','.')
 print "---> closing sftp connection. Done!"
 sftp.close
 print ""

