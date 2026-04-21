class Warrior:
    def __init__(self, health=100, stamina=100):
        self.health = health
        self.stamina = stamina
        
    # def __str__(self):        
    #     s1 = '---------------\n'
    #     s2 = f'Class: {self.__class__.__name__}\n'
    #     s3 = f'Health: {self.health}\n'
    #     s4 = f'Stamina: {self.stamina}\n'
    #     s5 = '---------------'
    #     return s1 + s2 + s3 + s4 + s5

    def __call__(self):        
        print('---------------')
        print(f'Class: {self.__class__.__name__}')
        print(f'Health: {self.health}')
        print(f'Stamina: {self.stamina}')
        print('---------------')


    def heals(self, target):
        print('---------------')
        print(f'{self.__class__.__name__} applies a bandage made of healing herbs to {target.__class__.__name__}')
        self.stamina -= 20
        target.health += 10
        print(f'Health of {target.__class__.__name__} increased to {target.health}',
            f'\n{self.__class__.__name__} has {self.stamina} stamina left')
        print('---------------')

    def __add__(self, target):
        if isinstance(target, Warrior) or isinstance(target, Mage):
            self.heals(target)
        elif isinstance(target, list):
            target.append(self)
            print(f"{self.__class__.__name__} has entered the group of {self.__class__.__name__}s")
        elif isinstance(target, int):
            self.health += target
            print("Health has been raised")

    def attacks(self, target):
        print('---------------')
        print(f'{self.__class__.__name__} deals damage with a sword to {target.__class__.__name__}')
        target.health -= 3
        print(f'Health of {target.__class__.__name__} decreased to {target.health}')
        print('---------------')
    
    def __sub__(self, target):
        if isinstance(target, Warrior) or isinstance(target, Mage):
            target.health -= 3
            print(f"{self.__class__.__name__} attacks {target.__class__.__name__}, he has {target.health} health left")
        elif isinstance(target, list):
            target.remove(self)
            print(f"{self.__class__.__name__} has left the group of {self.__class__.__name__}s")
        elif isinstance(target, int):
            self.health -= target
            print(f"Health has been decreased by {target}")


class Mage:
    def __init__(self, health=60, mana=120):
        self.health = health
        self.mana = mana
        
    def introduces(self):
        print('---------------')
        print(f'Class: {self.__class__.__name__}',
              f'\nHealth: {self.health}',
              f'\nMana: {self.mana}')
        print('---------------')


    def heals(self, target):
        print('---------------')
        print(f'{self.__class__.__name__} casts a healing spell on {target.__class__.__name__}')
        target.health += 10
        self.mana -= 20
        print(f'Health of {target.__class__.__name__} increased to {target.health}',
            f'\n{self.__class__.__name__} has {self.mana} mana left')
        print('---------------')


    def attacks(self, target):
        print(f'{self.__class__.__name__} deals damage with magic to {target.__class__.__name__}')
        target.health -= 3
        print(f'Health of {target.__class__.__name__} decreased to {target.health}')
        print('---------------')
    
unit1 = Warrior()
unit2 = Mage()
squad = []
unit1 - unit2
unit1 + squad
unit1 - squad
unit1 - 5
unit1 - 10