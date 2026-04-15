class Robot:
    
    def __init__(self, name, year, mental, physical):
        self.name = name
        self.year = year
        self.__mental = mental
        self.__physical = physical

    def get_condition(self):
        sum = self.__physical + self.__mental
        if sum <= -1:
            return "I feel unhappy!"
        elif sum > -1 and sum <= 0:
            return "I feel bad!"
        elif sum > 0 and sum <= 0.5:
            return "It could've been worse!"
        elif sum > 0.5 and sum <= 1:
            return "Everything seems to be alright!"
        else:
            return "Super!"

r1 = Robot("John", 1988, 0.2, 0.4)
r2 = Robot("Marcin", 1988, -0.4, 0.3)
print(r1.get_condition())
print(r2.get_condition())