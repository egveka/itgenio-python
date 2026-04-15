class Elevator:
    def __init__(self, floors=5, current=3):
        self.floors = floors
        self.current = current

    def up(self):
        if self.current != self.floors:
            self.current +=1
            print(f"The elevator moved 1 floor up, it is now on {self.current} floor!")
        else:
            print("The elevator is already on a maximum floor!")

    def down(self):
        if self.current > 0:
            self.current -=1
            print(f"Elevator moved 1 floor down, it is now on {self.current} floor")
        else:
            print("The elevator is already on a minimum floor!")

elev1 = Elevator(5, 0)
elev1.up()
elev1.up()
elev1.down()
elev1.down()
elev1.down()