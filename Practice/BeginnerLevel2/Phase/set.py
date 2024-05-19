#Set like List and tuple is can change Value but Dont has Dupilcate value include sort of value is Unknown (Gacha)
# mark is {} 

fruit = {"A1","A2","A3"}
print(fruit) #Gacha and Set (general) cannot access to allow index

fish = set({"AA","BB","CC"})
print(fish)
print(type(fish))

fruit.add(True) # not know index
fruit.add(3.99) # not know index
lis = ["hi","bro"] #add all info in 1 round
fruit.update(lis)
print("update = " + str(fruit))

fruit.discard("A1") 
# fruit.remove("A1") if you are using this function Even if dont has Info in variable It will Error
print("discard = " + str(fruit))


A1 = {"AAA","BBB","CCC"}
A2 = {"aaa","bbb","ccc"}
A3 = {"aaa","AAA","bbb","BBB","ccc","CCC"}
A = A1.copy()
print("A = " + str(A))
A.update(A2) # or ALL = A1.union(A2)
print("A = " + str(A))

diff1 = A2.difference(A1) # or A2.difference_update(A1)- not necessary has variable
diff2 = A1.difference(A2) # or A1.difference_update(A2)- not necessary has variable
intersec = A1.intersection(A3) # or A1.intersection_update(A3)- not necessary has variable
print("intersec A1 = " + str(intersec))
print("diff1 A2 = " + str(diff1))
print("diff2 A1 = " + str(diff2))


#it's have more that