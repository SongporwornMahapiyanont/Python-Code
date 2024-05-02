# number = int(input())
# name = input()
# check = True
# print(type(name))
# print(type(number))
# print(type(check))

# if number<19 and name=="Songporworn" :
#     check = False
# if number>=19 :
#     print(name)
#     print(check)
# elif check==True :
#     check = False
#     print(check)
# else :
#     print("The End")
#     print(15==20) #boolean


age = int(input())
level = int(input())
if age <18 :
    pass
elif age>=18 and age <30 :
    if level==2:
        print("Teen")
    else :
        print("xx")
elif age>=30 and age<60 :
    if level==3:
        print("man")
    else :
        print("xxx")
else :
    print("old") 
    
# print("children") if age>=15 else print("hi")