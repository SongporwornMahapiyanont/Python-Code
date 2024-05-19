
def CheckString (String) :
    result ={"Upper":0,"Lower":0,"Check":False}
    for i in String :
        if i.isupper() :
            result["Upper"]+=1
        elif i.islower() :
            result["Lower"]+=1
        else :
            result["Check"]=True
    return result

        
        
        
        
str = input()
x = CheckString(str)
print(x)