class Money:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents
        self.total_cents = dollars*100 + cents
    def get_dollars(self):
        return self.dollars
    def set_dollars(self, dollar):
        try:
            if dollar > -1:
                    self.total_cents += dollar * 100
            else:
                print("Error dollars")
        except TypeError:
            print("Error dollars")
    def get_cents(self):
         return self.cents
    def set_cents(self, cent):
        try:
            if cent > -1 and cent < 100:
                    self.total_cents += cent
            else:
                print("Error cents")
        except TypeError:
            print("Error cents")
    def __str__(self):
        return f"Your fortune is {self.dollars} and {self.cents}"
cash = Money(34, 77)
print(cash.get_dollars())
cash.set_dollars(1)
cash.set_dollars("Hello")
cash.set_dollars(-47)
print(cash.get_cents())
cash.set_cents(30)
print(cash.__str__())