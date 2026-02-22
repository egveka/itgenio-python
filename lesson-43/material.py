class Warrior:
    def __init__(self, health=100, stamina=100):
        self.stamina = stamina
        self.health = health
    
    def introduce(self):
        print("----------------")
        print(f"Class: {self.__class__.__name__}")
        print(f"Health: {self.health}")
        print(f"Stamina: {self.stamina}")
        print("----------------")
    
    def heal(self, target):
        print("----------------")
        print(f"{self.__class__.__name__} gives some smelly herbs",
              f"to {target.__class__.__name__}")
        target.health += 10
        self.stamina -= 20
        print(f"Health of {target.__class__.__name__} has been raised to {target.health}.", 
              f"\n{self.__class__.__name__} has {self.stamina} stamina points left!")
        print("----------------")
    
    def attack(self, target):
        print("----------------")
        target.health -= 3
        print(f"{self.__class__.__name__} does a sword attack to {target.__class__.__name__}",
              f"\nHealth of {target.__class__.__name__} has been decreased to {target.health}")
        print("----------------")

class Mage:
    def __init__(self, health=60, mana=100):
        self.mana = mana
        self.health = health
    
    def introduce(self):
        print("----------------")
        print(f"Class: {self.__class__.__name__}")
        print(f"Health: {self.health}")
        print(f"Mana: {self.mana}")
        print("----------------")

    def heal(self, target):
        print("----------------")
        print(f"{self.__class__.__name__} casts a healing spell!",
              f"to {target.__class__.__name__}")
        target.health += 10
        self.mana -= 20
        print(f"Health of {target.__class__.__name__} has been raised to {target.health}.", 
              f"\n{self.__class__.__name__} has {self.mana} mana points left!")
        print("----------------")
    
    def attack(self, target):
        print("----------------")
        target.health -= 3
        print(f"{self.__class__.__name__} does a magic attack to {target.__class__.__name__}",
              f"\nHealth of {target.__class__.__name__} has been decreased to {target.health}")
        print("----------------")

war = Warrior()
war.introduce()
mage = Mage()
mage.introduce()

mage.heal(war)
mage.heal(mage)
war.heal(war)
war.heal(mage)

war.attack(mage)
mage.attack(war)
mage.attack(mage)
mage.attack(mage)
mage.attack(mage)
mage.attack(mage)
mage.attack(mage)
mage.attack(mage)