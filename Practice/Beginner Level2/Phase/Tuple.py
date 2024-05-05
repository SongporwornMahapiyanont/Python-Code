#Tuple can not change value in itself. it's like List Just cannot change value of Varaible 
# but if you need to change value You must change tuple be List and then just change List be Tuple
# and Tuple can have Duplicate values include sort of value is Left to Right
# The mark of Tuple is ()

print("-----------")
tup1 = (1,2,3,4,"Songpor",True,4,4,4)
tup =(1,) #if you no use (,) Code will seen to tup is String.
tup8 = (12,8,31,4,121,3,41,421,1)


T = list(tup8) # Change Tuple to List
r = reversed(tup8)
print("reversed() = ",end=" ")
print(tuple(r)) # if you not change it. it will be Object - print(r)

T.sort()  # least to most
print(".sort() = " + str(tuple(T)))

T.reverse() # most to least
print(".reverse() = " + str(tuple(T)))

print("tup1 + tup = " + str(tup1+tup))
# tup2 = tuple(1.2,1,2,"String") 
# tup[0] = "String"  cannot change value in itself
print(tup1) 
print(tup1[1:4])

lis = list(tup1) # if you need do to about value in tuple. You will must tuple to list
# lis.remove( ? )
lis[0] = "hi"
print("Change value by list = " + str(tuple(lis)))
x = tup1.index(4)
y = tup1.count(4)
print(".index = " +  str(x)) # it will be first index to found.
print(".count = " + str(y)) # how much tup1 have number 4 ? 

print("-----------")


t = (1,2,3)
a,b,c = t
print(a,b,c) #output = 1 2 3

A1 = ('a','b','c')
A2 = ('A','B','C')

A1,A2 = A2,A1 # Switch value of A1 and A2 - Recommend must Run 
print("A1 , A2 = " + str(A1) + str(A2)) 
 
print("------------")


Charac = ('n','i','e')
str1 = "".join(Charac)
print("Charac = " + str("".join(Charac))) 

# for I in tup1 :
#     print(I,end=" ")
# print("")
# if "Songpor" in tup1 :
#     print("Songpor" in tup1)
    
# print("lengh = " + str(len(tup1)))


