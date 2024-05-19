number ={"191":"Police","999":"Me","1447":"Emergency"}

def CheckNumber (message):
    Check = False
    for Keys,Values in number.items():
        # print(Keys,Values)
        if Values == message:
            print(str(Values)+ " : ",Keys)
            Check = True
        if Keys == message :
            print(str(Keys)+" : ",Values)
            Check = True
    
    if Check == False :
        print("I Apologize, We do not have DATA ")
    
CheckNumber(input())