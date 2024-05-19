

number = int(input("start 1 To .... = "))
for i in range(1,number) :
    print("__________")
    print("number = ",i)
    for j in range(1,13):
        result = i*j
        print(str(i) + "x" + str(j) + " = " ,result,)
    # print("__________")