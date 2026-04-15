from random import randint

class Warrior:
    def __init__(self, health=100, stamina=100):
        self.__stamina = stamina
        self.__health = health

    def get_health(self):
        return self.__health
        
    def set_health(self, points):
        self.__health += points
        if self.__health > 100:
            self.__health = 100
        elif self.__health < 0:
            self.__health = 0

    
    def introduce(self):
        print("----------------")
        print(f"Class: {self.__class__.__name__}")
        print(f"Health: {self.__health}")
        print(f"Stamina: {self.__health}")
        print("----------------")
    
    def heal(self, target):
        if self.__stamina >= 20:
            print("----------------")
            print(f"{self.__class__.__name__} gives some smelly herbs",
                f"to {target.__class__.__name__}")
            target.set_health(+10)
            self.set_health(-20)
            self.__stamina -= 20
            print(f"Health of {target.__class__.__name__} has been raised to {target.get_health()}.", 
                f"\n{self.__class__.__name__} has {self.__stamina} stamina points left!")
            print("----------------")
        else:
            print("You dont have enough stamina to heal!")

# todo: change and move to knight

# todo: remove critical and move to knigh't attack
# same for mage LOL
    def attack(self, target):
        if target.get_health() > 3:
            print("Attack")
        else:
            print(f"The final blow is delivered by Warrior, and {target.__self__.__class__} is defeated.")

class Mage:
    def __init__(self, health=60, mana=100):
        self.__mana = mana
        self.__health = health

    def get_health(self):
        return self.__health
        
    def set_health(self, points):
        self.__health += points
        if self.__health > 100:
            self.__health = 100
        elif self.__health < 0:
            self.__health = 0
    
    def introduce(self):
        print("----------------")
        print(f"Class: {self.__class__.__name__}")
        print(f"Health: {self.health}")
        print(f"Mana: {self.mana}")
        print("----------------")

    def heal(self, target):
        if self.__mana >= 20:
            print("----------------")
            print(f"{self.__class__.__name__} casts a healing spell!",
                f"to {target.__class__.__name__}")
            target.set_health(+10)
            self.__mana -= 20
            print(f"Health of {target.__class__.__name__} has been raised to {target.get_health()}.", 
                f"\n{self.__class__.__name__} has {self.__mana} mana points left!")
            print("----------------")
        else:
            print("You dont have enough mana to heal!")

    def attack(self, target):
        chance2 = randint(1,100)
        if chance2 > 20:
            if target.get_health() > 3:
                print("----------------")
                target.set_health(-3)
                print(f"{self.__class__.__name__} does a magic attack to {target.__class__.__name__}",
                f"\nHealth of {target.__class__.__name__} has been decreased to {target.get_health()}")
                print("----------------")
            else:
                print(f"The final blow is delivered by Mage, and {target.__self__.__class__} is defeated.")

war = Warrior(100, 10)
mag = Mage()

war.heal(mag)
mag.heal(war)

war.attack(mag)
mag.attack(war)