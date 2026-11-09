plan = ["pilates", "yoga", "german", "spanish", "gym"]
print(plan)
print(plan[0])
print(plan[-1])
print(plan[1:4])
print(plan[:: -1])
plan[1] = "swimming"
print(plan)
plan.append("running")
plan.insert(0, "cooking")
print(plan)
plan.remove("running")
weekend = ["journalism", "photography"]
plan = plan + weekend
print(plan)
city = ("Berlin", "Germany", 50.11, 17.28)
print(city)
print(city[1])
print(city[-1])
print(type(city))
name, country, lat, lon = city
print(name)
print(lat)
city_list = list(city)
city_list[1] = "Germany"
print = tuple(city_list)
print(city)





