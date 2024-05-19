import random
 
for i in range(15) :
    x = random.random() # range 0.0-1.0 (float)
    y = random.uniform(5,10) # it can fix Range 
    z = random.randrange(1,10,2) # it can assign step
    a = random.randint(1,6) # random int
    O = [1,2,3,4,"a","b","x","c"]
    o = random.choice(O)
    random.shuffle(O) #print(O)
    print(a)
    