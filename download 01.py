import ftplib
import os

filename = "audio2.mp3"
ftp=ftplib.FTP()
ftp.connect("183.111.174.9",21)
ftp.login("tndusdl73","qlalf357")
ftp.cwd("/home/pi")
fd = open("./" + filename,'wb')
ftp.retrbinary("RETR " + filename, fd.write)
fd.close()