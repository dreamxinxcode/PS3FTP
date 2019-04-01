from ftplib import FTP
import configparser
from time import sleep

config = configparser.ConfigParser()
config.read("config.ini")

eboot = config.get("eboot", "filename")
ebootdir = config.get("eboot", "directory")
sprx = config.get("eboot", "filename")
sprxdir = config.get("sprx", "directory")

test = config.get("test", "filename")
testdir = config.get("test", "directory")

global directory
directory = "~/"

def connect():
    ps3IP = input("Enter PS3 IP: ")
    print("[\033[95m*\033[0m] Connecting to: " + ps3IP)
    global ftp
    ftp = FTP(ps3IP)
    ftp.login()
    print("[\033[95m*\033[0m] Connected")
    print("[\033[95m*\033[0m] Listing PS3 root directory")
    ftp.retrlines('LIST')
    print("[\033[95m*\033[0m] Done")

def listDir():
    ftp.retrlines('LIST')

def listTMP():
    ftp.cwd("/dev_hdd0/tmp")
    ftp.retrlines('LIST')

def changeDirectory():
    directory = input("Directory: ")
    ftp.cwd(directory)
    ftp.retrlines('LIST')
    print("[\033[95m*\033[0m] Changed to " + directory)

def upload():
    filename = input("Enter file to upload: ")
    print("[\033[95m*\033[0m] Uploading: " + filename)
    ftp.storbinary('STOR '+filename, open(filename, 'rb'))
    print("[\033[95m*\033[0m] Done")
    ftp.quit()

def installSPRX():
    ftp.cwd(testdir)
    ftp.storbinary('STOR '+test, open(test, 'rb'))
    ftp.quit()

def delete():
    filename = input("File to delete: ")
    ftp.delete(filename)

loop = True

while loop == True:
    option = input("""\033[95m
:ooooooooooo+++++:.          .:+++++++++-  ++++++++++++++++/:`
.::::::::::::::/oNNo        :mMs////////.  ///////////////+hMm-
                 mMm        sMM.                           -MMo
 -/ossssssssssssyNd:        sMM.           ssssssssssssssssmMd.
:NMs:------------.`         sMM.           ---------------:yMm-  
sMM.                        sMM.                           .MMs    
sMM.               /++++++++mNh`           ++++++++++++++++dNd.      
:oo`               /////////:-             ////////////////:-\033[0m
			             Developed by: \033[95mdream.in.code\033[0m\n
###############################################################\n
       [\033[95m1\033[0m] Connect              [\033[95m6\033[0m] Upload File
       [\033[95m2\033[0m] Install SPRX         [\033[95m7\033[0m] Delete File
       [\033[95m3\033[0m] Install EBOOT.BIN    [\033[95m8\033[0m] Disconnect
       [\033[95m4\033[0m] List Directory       [\033[95m9\033[0m] Help
       [\033[95m5\033[0m] Change Directory     [\033[95m10\033[0m] Exit\n
###############################################################\n\n"""
+ "\033[95m┌─╼ \033[0m" + "root " + "\033[95m╺─╸ \033[0m" + "playstation " + "[\033[95m" + directory + "\033[0m]\n" + "\033[95m└────╼ \033[0m""")
    
    option = int(option)

    if option == 1:
        connect()
    elif option == 2:
        installSPRX()
    elif option == 3:
        connect()
    elif option == 4:
        listDir()
    elif option == 5:
        changeDirectory()
        ftp.retrlines('LIST')
    elif option == 6:
        placeFile()
    elif option == 7:
        delete()
    elif option == 8:
        ftp.quit()
    elif option == 9:
        documentation()
    elif option == 10:
        ftp.quit()
        exit(0)


