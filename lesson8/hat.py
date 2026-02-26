import random
class Hat:
    def __init__(self):
        self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    @classmethod
    def sort(cls, name):
        print(f"{name} is in {random.choice(cls.houses)}")


Hat.sort("harry")