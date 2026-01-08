def find_speed(km, h):
    m = km * 1000
    sec = h * 60 * 60
    speed = round(m / sec, 2)
    return speed

x = find_speed(100, 3)
print(x)