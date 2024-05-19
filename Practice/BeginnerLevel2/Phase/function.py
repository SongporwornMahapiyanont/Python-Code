def Calcualate (x,name) : #parameter
    # print("hello ", 10 , " hi") 
    # print("hello = " + x) #Agrument
    h = " "
    if x % 2 ==0 :
        print("even",end=" ")
        h = "even"
    else :
        print("odd",end=" ")
        h = "odd"
    print("hi = " + name + " " + str(x) + " " + h,end="")
    print(" end ")
    
def Test(*args) : # name can fix and Parameter has it nemerous
    print("------")
    print(args)
    for i in range(len(args)) : 
        print(args[i])
        
def TestDicInfo(**kwargs) : # name can fix and Info in itself is 'Dictionary' and Parameter has nemerous Key 
    print(kwargs)
    for i in kwargs.values() : 
        print(".value() = " + str(i))

def InfoCity(name,lname,City="Bangkok") :
    print("name = " + name)
    print("lname = " + lname)
    print("City = " + City)

def Array(item) : # input is List
    for i in range(len(item)) : 
        print("item [" + str(i) + "] " + str(item[i])) #if you must necesary to 'print' I recommend tranform to str()

def Back(x,y,z) :
    if x==0 and y==0 and z==0 : 
        return True
    elif x<=9 or y<=9 or z<=9 :
        return 
    return x+y+z
        
def PASS():
    pass


# print("_____________")

# x = int(input()) 
# name = input()
# Calcualate(x,name) #Agrument

# print("_____________")

# Test(1)
# Test(12,12)
# Test(12,321,124)

# print("_____________")

# InfoCity(City="thai",lname="mahapiyanont",name="Songporworn")
# InfoCity(name="Songporworn",lname="Mahapiayanont")

# print("_____________")

# item =["HI",234,True]
# ITEM = ("asddsafs",32121,False)
# Array(item)s
# print()
# Array(ITEM)

# print("_____________")

# print("Back = " + str(Back(12,13,14)),end="   ")
# print("Back = " + str(Back(2,3,4)),end="   ")
# print("Back = " + str(Back(0,0,0)))

# print("_____________")

# TestDicInfo(fname="SOngporworn",age=19)
# print()
# TestDicInfo(fname="Nine",age=15)
# print()
# TestDicInfo(fname="OOOO",age=99)

