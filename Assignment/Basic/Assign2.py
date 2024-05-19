
temp = input("Input Value and C or F : ")

Degree = temp[:-1]  #temp[:len(temp)-1] 
print("D = ",Degree)
Unit = temp[-1].lower()
print("U = ",Unit)

if Unit == "C" or Unit =="c":
    print("C = ",Degree)
elif Unit == "D" or Unit == "d" :
    print("U = ",Degree)
else :
    print("Error")