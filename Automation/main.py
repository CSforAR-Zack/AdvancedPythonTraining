from os import system
from time import sleep

system("python zippedFileCreator.py")
sleep(2)
system("python fileUnzipper.py")
sleep(2)
system("python fileDeleter.py")
