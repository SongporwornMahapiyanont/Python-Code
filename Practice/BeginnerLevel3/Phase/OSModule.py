import os #this module is manage about file for examble remove ,fix file

try :
    if os.path.exists("D:\Python-Code\Practice\Beginner Level3\Phase\GarbageFile.txt") : # This code is research for Do have you file? - You have = True , You have not = False
        os.remove("D:\Python-Code\Practice\Beginner Level3\Phase\GarbageFile.txt")
    else :
        print("do not found file")
except Exception as E:
    print(E)