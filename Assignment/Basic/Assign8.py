# Dictionary

Market = {"number" : 
            {"one" :{
                "name" :"Songporworn",
                "manu" :["Chiken","meat","Pig"],
                "zone" : "1",
                },
             "two":{
                "name" :"Mahapiyanont",
                "manu" : {"game":["Godofwar","ASs","Sekiro"],"exercise":"Gym"},
                "zone" : "2"
             }
            }
}

# print(Market["number"]["1"])
# print(Market["number"]["2"])
# print(Market["number"]["2"]["manu"]["game"][:len("game")])
# print(Market["number"]["2"]["manu"]["game"][:len("game")] == "Godofwar" )
# print(Market["number"]["2"]["manu"]["game"][:len("game")])

for i in Market["number"]["two"]["manu"].values() :
    if i == "Gym" :
        print("Hello")
    print(i)
