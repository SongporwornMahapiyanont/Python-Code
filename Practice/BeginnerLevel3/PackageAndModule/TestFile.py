import MainProgram as Main # or from MainProgram import * 
from MainProgram import addition as add

print("________________")
Main.addition(10,20,30) # This code can work from line 1
Main.addition(1,2,3,4,5,6,7,8) # This code can work from line 1
Main.addition(int("2"),int("3"),int("4")) # This code can work from line 1
add(1,2,3,45,5) # This code can work from line 2
print("________________")