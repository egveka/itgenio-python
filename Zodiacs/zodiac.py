def define(day, month):
    zodiac = month
    if day > 31 or month > 12:
        return 0
    elif day <= 31 and month <= 12:
        if day >= 22:
            zodiac += 1
            if zodiac == 13:
                zodiac = 1
    return zodiac