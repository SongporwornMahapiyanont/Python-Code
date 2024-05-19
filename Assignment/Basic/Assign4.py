def MaxValue(x,y) :
    if x>y :
        return x
    elif x<y :
        return y
    else :
        return x
def MinValue(x,y) :
    if x>y :
        return y
    elif x<y :
        return x
    else :
        return x
    
X = int(input("input int : "))
Y = int(input("input int : "))
print("Max = ",MaxValue(X,Y))
print("Min = ",MinValue(X,Y))