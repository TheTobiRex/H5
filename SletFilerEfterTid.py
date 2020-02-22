import os
from os import listdir
from os.path import isfile, isdir, join
import os.path, time
import platform
import time

def creation_date(path_to_file):
    if platform.system() == 'Windows':
        return os.path.getmtime(path_to_file)
        #return time.ctime(os.path.getmtime(path_to_file))
    else:
        return print("This script is not cross-platform, please use it on Windows as intended")

defaultpath = "C:\\users\\Tobias\\Desktop"

print("Input the path to the desired directory (It will default to your desktop if nothing is written): ")
mypath = input()

if mypath == "":
    mypath = defaultpath
    print("Du indtastede ikke nogen værdi, vender tilbage til standart: %s" % defaultpath)
else:
    if isdir(mypath):
        print("Din sti er godkendt")
    else:
        while isdir(mypath) == False:
            print("Stien du indtastede kunne ikke findes i systemet, prøv venligst igen.")
            mypath = input()


for f in listdir(mypath):
    fullpath = join(mypath, f)
    if isfile(fullpath):
        #print(f + ":")
        #print(creation_date(fullpath))

        result_month = (time.time() - creation_date(fullpath)) / 2629743
        result_week = (time.time() - creation_date(fullpath)) / 604800
        #print(result)

        if result_month > 1:
            print("Filen %s bliver slettet" % f)

        if result_week > 1 and result_month < 1:
            print("Filen %s bliver zippet" % f)
