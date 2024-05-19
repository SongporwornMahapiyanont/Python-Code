#Dict not necessary for remember index of value Just use key for resourse

color = {"red":"apple" , "yellow":"banana", 115:"house"}
animal = dict({"m":"monkey"})
print(color["red"],color[115])
print(animal["m"])

color[115] = "home" #fix
print(color[115]) 
color.update({"blue":"sky"})
print("color = " + str(color))
print(" ")

for item in color.items() : 
    print(item,end=" ")
print(" ")
for item in color.values() :
    print(item,end=" ")
print(" ")
for item in color.keys() :
    print(item,end=" ")
print(" ")
print(" ")

color.pop("red")
print(color)
color.popitem()
print(color)

print(" ")

market = {"food":{"name": "nine" , "manu":"banana" , "zone":"A2"},"food2":{"name": "near" , "manu":"apple" , "zone":"A3"}}
print(market["food"]["manu"])
print(market["food2"]["manu"])