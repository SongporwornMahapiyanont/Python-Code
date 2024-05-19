num = int(input("Input Value : "))
period = int(input("Input Period : "))
for i in range(1,num+1,period) :
    for j in range(1,num+1,period) :
        print(str(j)+"-",end="")
    print("")