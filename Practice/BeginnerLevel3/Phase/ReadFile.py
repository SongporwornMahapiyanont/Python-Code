
try :
    # open(namefile or Address file ,mode(r=read,w=write,a=append,t=txtfile,b=binaryfile), access password (for languese to code cannot read for example Thai))
    fr = open("D:\Python-Code\Practice\Beginner Level3\Phase\Text.txt","r",encoding="utf-8")
    # r = open("D:\Python-Code\Practice\Beginner Level3\Phase\Text.txt","r",encoding="utf-8")
    print("--------------------")
    # print(fr.read())
    # print(fr.readline())
    print(fr.readlines())
    # fr.write() mode will fix be "w" or "a"
    # fr.writelines() mode will fix be "a" or "w"
    print("--------------------")
    fr.close()
except Exception as E:
    print("--------------------")
    print("Error because = " + str(E))