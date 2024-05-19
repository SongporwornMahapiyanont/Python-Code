while True : 
    number1 = int(input("input your number = "))
    number2 = int(input("input your number = "))
    try :
        result = float(number1/number2)
        if number1<0 or number2 <0 :
            break
        if number1==10 and number2==10 :
            raise Exception("sdkjfajgadwslkjfv")
        print(format(result,'.2f'))
    except Exception as E: 
        print("Error from " + str(E))
    # except ValueError :
    #     print("Error")
    # except ZeroDivisionError :
    #     print("Dont / to zero")
    # except TypeError :
    #     print("typr error")
    
    # finally : # When code no Error finally will Next started work.  
    #     result+=10
    #     print(result)

    else : 
        print("Finished")

    