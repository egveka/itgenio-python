class Rectangle:
    def __init__(self, a=10, b=5):
        self.a = a
        self.b = b
    def calculate_area(self):
        return f"Area = {self.a * self.b}"
    def draw(self):
        for _ in range(self.b):
            print("*" * self.a)
        print()

r1 = Rectangle()
r2 = Rectangle(5,3)
print(r1.calculate_area())
print(r2.calculate_area())

r1.draw()
r2.draw()
