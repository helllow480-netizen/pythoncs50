class Cat:
    MEOWS = int(input("How many times should the cat meow? "))
    def meow(self):
        for i in range(self.MEOWS):
            print("Meow")

cat = Cat()
cat.meow()