from material import Warrior, Mage
from random import randint

class Knight(Warrior):
    def __init__(self, health=100, armor=100, stamina=100):
        super().__init__(health, stamina)
        self.__health = health
        self.__armor = armor

    def set_health(self, points):
        self.__health += points
        if points > 0:
            super().set_health(points)
        else:
            if self.__armor >= abs(points):
                self.__armor += points
                print(f"Armor of {self.__class__.__name__} has been decreased to {self.__armor}")
            else:
                self.__health += points
                print("Armor has been destroyed")
                print(f"Health of {self.__class__.__name__} has been decreased to {self.__health}")
        def __critical_hit(self, target):
            target.set_health(-10)

        def attack(self, target):
            chance = randint(1,100)
            if chance > 40:
                target.set_health(-3)
                print("Knight atatcks with sword")
            else:
                self.__critical_hit(target)
                print("Critical hit!")

class Wizard(Mage):
    def __init__(self, health=60, mana=100, barrier = 100):
        super().__init__(health, mana)
        self.__barrier = barrier

        def set_health(self, points):
            self.__health += points
            if points > 0:
                super().set_health(points)
            else:
                if self.__barrirer >= abs(points):
                    self.__barrier += points
                    print(f"barrier of {self.__class__.__name__} has been decreased to {self.__barrier}")
                else:
                    self.__health += points
                    print("barrier has been destroyed")
                    print(f"Health of {self.__class__.__name__} has been decreased to {self.__health}")

    def __fire_ball(self, target):
            target.set_health(-15)

    def attack(self, target):
        chance = randint(1, 100)
        if chance > 40:
            target.set_health(-3)
            print("wizard attacks")
        else:
            self.__fire_ball(target)
            print("Critical hit!")
    
# k1 = Knight(50,50,50)
# k2 = Knight(50,0,50)
# print(k1.__dict__)
# k1.attack(k2)

w1 = Wizard(60, 100, 0)
w2 = Wizard(60, 100, 0)
w1.attack(w2)