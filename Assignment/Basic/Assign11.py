import random

ATM_PASSWORD = "Songporworn12394123"
result = ""
while result!=ATM_PASSWORD :
    result = ""
    for letter in range(len(ATM_PASSWORD)) :
        list_number = random.choice("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        result = "".join(list_number)+str(result)
        print("SEARCH = " ,result)
print("Crack password is : ",result)