class Animal:
    def make_sound(self):
        print("Some sound")
    
    def printMe(self):
        print("hi")

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

    def wag_tail(self):
        print("Tail wagging")

dog = Dog()
animal : Animal = dog  # Implicitly treated as Animal

animal.make_sound()  # Calls ovverriden method in Dog: Woof!
animal.wag_tail()    # Still works in Python because of dynamic typing
