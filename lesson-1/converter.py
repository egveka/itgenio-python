user_number = float(input("Give me a number of meters: "))

unit_type = input("Length unit (cm or km): ")

if unit_type.lower() in ["centimeter", "cm"]:
    print(user_number * 100, unit_type)
elif unit_type.lower() in ["kilometer", "km"]:
    print(user_number / 1000, unit_type)
else:
    print(user_number, "m")