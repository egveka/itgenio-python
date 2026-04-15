from material import Warrior, Mage

class Archer(Warrior):
    def __init__(self, health=100, stamina=100, arrows=20):
        super().__init__(health, stamina)
        self.arrows = arrows
    def attack(self, target):
        print("----------------")
        print(f"{self.__class__.__name__} does a sword attack to {target.__class.__name}")
        target.health -= 4
        self.arrows -= 1
        print(f"{self.__class__.__name__} does a bow attack to {target.__class__.__name__}",
              f"\nHealth of {target.__class__.__name__} has been decreased to {target.health}")
        print(f"{self.__class__.__name__} used 1 arrow from his quiver. {self.__class__.__name__} has {self.arrows} left")
        print("----------------")

unit1 = Archer()
unit2 = Archer()

print(unit1.__dict__)
unit1.introduce()
unit2.heal(unit1)
unit1.attack(unit2)

class Alchemist(Mage):
    def __init__(self, health=100, mana=100, flasks = 10):
        super().__init__(health, mana)
        self.flasks = flasks
    def attack(self, target):
        print("----------------")
        target.health -= 10
        self.flasks -= 1
        self.health -= 3
        print(f"{self.__class__.__name__} does a magic flask to {target.__class__.__name__} but hurts himself in the process",
            f"\nHealth of {target.__class__.__name__} has been decreased to {target.health}")
        print(f"Health of {self.__class__.__name__} has been decreased to {self.health}")
        print(f"{self.__class__.__name__} used 1 flask from his inventory. {self.__class__.__name__} has {self.flasks} left")
        print("----------------")

unit3 = Alchemist()
unit3.attack(unit2)