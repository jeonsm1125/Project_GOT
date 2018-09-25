import ftplib
import os

filename = "micTest.wav"
ftp=ftplib.FTP()
ftp.connect("183.111.174.9",21)
ftp.login("tndusdl73","qlalf357")
ftp.cwd("./")
os.chdir(r"/www/tndus")
myfile = open(filename,'rb')
ftp.storbinary('STOR ' +filename, myfile )
myfile.close()
ftp.close