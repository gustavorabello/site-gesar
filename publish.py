## =================================================================== ##
#  this is file test.py, created at 27-Apr-2014                #
#  maintained by Gustavo Rabello dos Anjos                              #
#  e-mail: gustavo.rabello@gmail.com                                    #
## =================================================================== ##


import paramiko,os
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

def upload(source,destination):
 sftp.put(source,destination)


if __name__ == "__main__":
 path='/paginas'
 rm(path)
 #upload('.','.')
 sftp.close

