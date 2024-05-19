# Program for Calculate BMI
print("__Welocome to Program Calculate BMI__")
try :
    for i in range(5) :
        Weight = float(input("Input your weight (Kg) : "))
        High = float(input("Input your high (Cm): "))
        High = High/100
        BMI = Weight/High**2
        print("Your BMI["+str(i)+"] : ",format(BMI,'.3f'))
        if BMI >=100 :
            print("OverWeight : ",format(BMI,'.3f'))
        else :
            print("GeneralWeight : ",format(BMI,'.3f'))
except Exception as E:
    print("Error : ",E)
print("__The End__")