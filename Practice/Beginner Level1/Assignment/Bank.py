Cash = float(input())

Cash1000 = 0 
Cash500 = 0
Cash100 = 0
Cash50 = 0
Cash20 = 0
Cashetc = 0

while True :    
    if Cash>=1000 :
        print("1000 = " + str(Cash//1000))
        Cash%=1000
    elif Cash>=500 and Cash<1000 :
        print("500 =" + str(Cash//500))
        Cash%=500
    elif Cash>=100 and Cash<500 :
        print("100 =" + str(Cash//100))
        Cash%=100
    elif Cash>=50 and Cash<100 :
        print("50 = " + str(Cash//50))
        Cash%=50
    elif Cash>=20 and Cash<50 :
        print("20 = " + str(Cash//20))
        Cash%=20
    else :
        
        print("remain Cash = " + str(Cash))
        break
    