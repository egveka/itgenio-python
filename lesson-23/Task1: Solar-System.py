solar_system = {}
solar_system["Sun"] = 1300000
solar_system["Mercury"] = 0.05
solar_system["Venus"] = 0.86
solar_system["Earth"] = 1
solar_system["Mars"] = 0.15
solar_system["Jupiter"] = 1321
solar_system["Saturn"] = 764
solar_system["Uranus"] = 63
solar_system["Neptune"] = 57.7
solar_system["Pluto"] = 0.059

solar_system.pop("Pluto")

print(solar_system)

# for key in solar_system.keys():
#     print(key)

# for value in solar_system.values():
#     print(value)

for key,value in solar_system.items():
    if value > 1:
        print(key)

for key,value in solar_system.items():
    if key[0] == "M":
        print(value)