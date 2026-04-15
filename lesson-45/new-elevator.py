from elevator import Elevator

class NewElevator(Elevator):
    def __init__(self, floors=5, current=3):
        super().__init__(floors, current)
        
    def move(self, to):
        if to <= self.floors:
            print(f"Moving the elevator from {self.current} to {to}!")
            self.current = to
            print(f"Elevator is now at {self.current}")
        else:
            print("The elevator cant move on that floor!")

ele1 = NewElevator(10, 3)
ele1.move(9)
ele1.move(11)