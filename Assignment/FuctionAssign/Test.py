import System


try : 
    account = {}
    num = int (input("How many User : "))
    for i in range(num) :
        name = input("Input All Name User : ")
        account.update({name:0})
        print(account)
    while True :
        print("________________________")
        print("")
        user = input("input your name : ")
        order = input("Input your order (G = Output Your Money , d = deposit , w = withdraw , t = tranfer , etc.=break) : ")

        if order == "G" :
            System.GetBalance(user)
        elif order == "d" :
            money = int(input("input your money : "))
            System.deposit(user,money)
        elif order == "w" :
            money = int(input("input your money : "))
            System.withdraw(user,money)
        elif order == "t" :
            money = int(input("input your money : "))
            System.tranfer(user,money)
        else :
            break
except Exception as E:
    print("Error : " ,E)