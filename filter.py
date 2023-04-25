
#filters

friends =[("Bobby", 20),
          ("Paul", 30),
          ("Jared", 23),
          ("Shane", 18),
          ("Ramon", 29)]

age = lambda data:data[1] >= 21

drinking_buddies = list(filter(age, friends))

for i in drinking_buddies:
    print(i)