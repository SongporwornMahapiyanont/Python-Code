import Test
def GetBalance(name) :
    print("Money " + name +" = ",Test.account[name])
    print("_______________")

def deposit(name,money) :
    print("Name : ",name)
    print("deposit : ",money)
    for i in Test.account.keys() :
        if i == name :
            Test.account[name]+=money
    print("_______________")
            
def withdraw(name,money) :
    print("withdraw : ",money)
    for i in Test.account.keys() :
        if Test.account[name]>=money :
            if i == name :
                Test.account[name]-=money
        else :
            print("__Your Money not Enough__")
    print("_______________")

def tranfer(user,money) :
    name = input("Who is your tranfer : ")
    for i in Test.account.keys() :
        if Test.account[user]>=money : 
            if i == name :
                Test.account[name]+=money
                Test.account[user]-=money
        else :
            print("__Your Money not Enough__")
    print("_______________")
