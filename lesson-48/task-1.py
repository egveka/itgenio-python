class CreditCard:
    def __init__(self, name, number, pin, balance):
        self.name = name
        self.__number = number
        self.__pin = pin
        self.__balance = balance
    def info(self):
        pin_inp = input("Input your pin: ")
        name_inp = input("Input your name: ")
        if pin_inp == self.__pin and name_inp == self.name:
            print(self.__balance)
            print(self.__number)
        else:
            print(f"############{self.__number[-1]}{self.__number[-2]}{self.__number[-3]}{self.__number[-4]}")
    def operation(self, money, op):
            if op == "withdraw":
                if money <= self.__balance:
                    self.__balance -= money
                else:
                    print("not enough money!")
            elif op == "deposit":
                self.__balance += money
c1 = CreditCard("Guy", "12345678910111213141516", "41235", 10000)
c1.info()
c1.operation(500, "withdraw")
c1.info()