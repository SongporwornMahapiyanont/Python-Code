#Recursive Function is Function about cally itself (Function itself) 

def Remove(value):
    if value >= 5 :
        print("The end")
        return
    value+=1
    print("value = " + str(value))
    Remove(value)
# value = int(input())
# Remove(value)

def summary(V):
    if V>=100:
        return
    V+=V
    print("V = " + str(V))
    summary(V)
# V = int(input())
# summary(V)


def factoral(number):
    if number<=1 :
        return number
    print("number = " + str(number))
    return number * factoral(number-1) #it will protect Info to Ram But function will keep worked and the end when condition finished 
    #and value of Calculated will comeback when function finished or It is 'print(factoral(number))'
    

number = int(input())
x = factoral(number)
print("result = ",end=" ")
# print(factoral(number)) Dont do it because Function factoral will worked 2 time. it is line 32 and 34 because factoral(...) is called using function
print(x)