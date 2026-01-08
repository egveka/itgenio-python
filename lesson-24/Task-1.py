countries_cities = {"Germany":["Berlin", "Dortmund", "Leverkusen", "Munich"],
                    "England":["London", "Liverpool", "Manchester", "Brighton"],
                    "Russia":["Moscow","St. Petersburg", "Borisoglebsk", "Sochi"],
                    "Spain":["Barcelona", "Madrid", "Valencia", "Bilbao"]}

city = input("Give me a city\n")

for key,value in countries_cities.items():
    if city in value:
        print(key)
        break
else:
    print("City not found")