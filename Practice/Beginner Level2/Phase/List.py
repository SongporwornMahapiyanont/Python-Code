# datatype (List) it's can fix value in itself
# and List can has Duplicate values include sort of value  is Left to Right 
# The mark of List is []

# info = [1,"String",True,1.0]
# print(type(info))
# print(info[1:3])
# print(info[-1])
# print(info[1:])
# print(info[:3])

# if 1 in info :
#     print(1 in info)
# else :
#     print(not 1 in info)


info1 = [1,2,3,4,5,6,7,8,9,0,0,0,0,0]
info2 = ["a","b","c","c","d"]

info1.append(12)
info2.append("AA")
print(info1)
print(info2)

print("-------------------")

info1.insert(2,2)
info2.insert(2,"bb")
print(info1)
print(info2)

print("-------------------")

info1.remove(0) #remove first value
print(info1)
info2.pop() #remove new value
print(info2)
del info1[1]
print(info1)
del info1 #this is delete value and varible
# print(info1) 
info2.clear() # clear all value in variable 
print("info2 = " + str(info2))

print("-------------------")

INFO = [1,1,1,1,1,1,1,1,1,1]
x = INFO #info of x will change like info
X = INFO.copy() #clone
INFO.clear()
print(x)
print(X)

print("-------------------")

a = [2,2,2,2,2,2,2,2,2]
b = [3,3,3,3,3,3,3,3,3]
zq =["String"]
result = a+b
result = print(result)
c = a.count(2)
print(c)

a.extend(zq)
print(a)