name = input()
print("------------")

print("index start = " + name[0])
print("index start to stop : = " + name[0:4]) #or print(name[:4])
print("lastindex = " + name[-1])
print(len(name)) # it will sum (_) 

print("------------")

print(name)
print("strip = " + name.strip()) #or rstrip (right) or lstrip (left)
print(len(name)) #lengh of String

print("------------") 

print(name.upper()) # SALDASNLDASD
print(name.lower()) # asdnasldjasdn
print(name.capitalize()) # Sasdansdlkjasn

print("------------") 

print("replace = " + name.replace("Song","Neur",2)) #replace word  and how much time to replace

print("------------")

s = "Song" in name #Request word in String , output is boolean
print(s)

print("------------")

text = "Name : {} \t lastname :{}"
print(text.format("Song","nonor"))

print("------------")

fruit = "apple banana apple"
print("apple = " + str(fruit.count("apple")))

print("------------")

NAME = "MR.appleNongnear"
print(NAME.startswith("MR."))
print(NAME.endswith("near"))

print("------------")