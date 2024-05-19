def result(*args):
    result = ValueMax(ValueMax(ValueMax(ValueMax(ValueMax(x,y),z),a),b),c)
    print("MAX : " + str(result))
    # return result

def ValueMax (x,y) :
    if x>y :
        return x
    elif y>x :
        return y
    else :
        return 0    
    
x,y,z,a,b,c = map(int,input().split())
result(x,y,z,a,b,c)