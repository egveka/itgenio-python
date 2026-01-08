years = int(input())

beautiful_year = False
counter = years
while beautiful_year == False:
    counter += 1
    years_s = set(str(counter))
    if len(years_s) == 4:
        print(counter)
        beautiful_year = True