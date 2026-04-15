from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, a=3):
        super().__init__(a,a)
s1 = Square()
s1.draw()

print(s1.calculate_area())