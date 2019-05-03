from ftplib import FTP
import configparser
import requests
import urllib.request, urllib.error
import os
import socket
import sys
from time import sleep

config = configparser.ConfigParser()
config.read("config.ini")

#eboot = config.get("eboot", "filename")
#ebootdir = config.get("eboot", "directory")
#sprx = config.get("sprx", "filename")
#sprxdir = config.get("sprx", "directory")

test = config.get("test", "filename")
testdir = config.get("test", "directory")

global menu
global ccapiMenu
global directory
directory = "~/"

def connect():
    global ps3IP
    ps3IP = input("\033[95m \033[1mEnter PS3 IP: \033[0m")
    print("[\033[95m*\033[0m] Connecting to: " + ps3IP)
    success = ['http://'+ps3IP+':6333/ccapi/ringbuzzer?type=1', 'http://'+ps3IP+':6333/ccapi/notify?id=2&msg=Connected']
    try:
        for url in success:
            urllib.request.urlopen(url)
    except urllib.error.URLError as e:
        print("Fuck")
    except socket.timeout as e:
        raise MyException("There wa   s an error: %r" % e)
         
    global ftp
    ftp = FTP(ps3IP)
    ftp.login()
    print("[\033[95m*\033[0m] Connected")
    print("[\033[95m*\033[0m] Listing PS3 root directory")
    ftp.retrlines('LIST')
    print("[\033[95m*\033[0m] Done")

def listDir():
    ftp.retrlines('LIST')
    urllib.request.urlopen('http://'+ps3IP+':6333/ccapi/notify?id=2&msg=No ps3 for scott XD')
    firmware = urllib.request.urlopen('http://'+ps3IP+':6333/ccapi/getfirmwareinfo').read()
    temp = urllib.request.urlopen('http://'+ps3IP+':6333/ccapi/gettemperature').read()
    print(firmware)
    print(temp)

def listTMP():
    ftp.cwd("/dev_hdd0/tmp")
    ftp.retrlines('LIST')

def changeDirectory():
    directory = input("\033[95m \033[1mDirectory: \033[0m")
    ftp.cwd(directory)
    ftp.retrlines('LIST')
    print("[\033[95m*\033[0m] Changed to " + directory)

def upload():
    filename = input("\033[95m \033[1mEnter file to upload: \033[0m")
    print("[\033[95m*\033[0m] Uploading: " + filename)
    ftp.storbinary('STOR '+filename, open(filename, 'rb'))
    print("[\033[95m*\033[0m] Done")

def installSPRX():
    ftp.cwd(testdir)
    ftp.storbinary('STOR '+test, open(test, 'rb'))
    ftp.quit()

def delete():
    filename = input("\033[95m \033[1mFile to delete: \033[0m")
    ftp.delete(filename)

ccapiMenu = False
    
while ccapiMenu == True:
    ccapiOption = input("""
###############################################################\n
           [\033[95m1\033[0m] Console ID & PSID    [\033[95m6\033[0m] Upload File
           [\033[95m2\033[0m] Console Power        [\033[95m7\033[0m] Delete File
           [\033[95m3\033[0m] Notification Options [\033[95m8\033[0m] Disconnect
           [\033[95m4\033[0m] Console Information  [\033[95m9\033[0m] Help
           [\033[95m5\033[0m] Buzzer Options       [\033[95m10\033[0m] Exit\n
###############################################################\n\n"""
+ "\033[95m┌─╼ \033[0m" + "root " + "\033[95m╺─╸ \033[0m" + "playstation " + "[\033[95m" + directory + "\033[0m]\n" + "\033[95m└────╼ \033[0m""")
    
    ccapiOption = int(ccapiOption)

    if ccapiOption == 1:
        print("TEST")
        beep()
    elif ccapiOption == 3:
        installSPRX()
    elif ccapiOption == 4:
        installSPRX()
    elif ccapiOption == 5:
        installSPRX()
    elif ccapiOption == 6:
        installSPRX()
  

def beep():
    urllib.request.urlopen("http://"+ps3IP+":6333/ccapi/ringbuzzer?type=1")

menu = True

while menu == True:
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
           [\033[95m3\033[0m] Install EBOOT.BIN    [\033[95m8\033[0m] CCAPI
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
    elif option == 6:
        upload()
    elif option == 7:
        delete()
    elif option == 8:
        menu = False
        ccapiMenu = True
    elif option == 9:
        beep()
    elif option == 10:
        ftp.quit()
        exit(0)

