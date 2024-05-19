x = 10
y = 2
a = 9
s = "20"
# print(x+y+a) it's Cannot run

result = x+y+a
print("result = " + str(result))
result+=int(s)
print(result)

result=str(result)

print("String = " + result)


print("Result1 = " , x+y , " " , x*y)
print("Result2 = " , x/y , " " , x//y)
print("Result3 = " , 123%y) 
print("Result4 = " , x**3 )


BB = 1.555552323141124
print(format(BB,'.2f'))