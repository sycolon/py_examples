from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, brand):
        self.brand = brand

    @abstractmethod
    def hello(self):
        pass
       # print("This is a generic vehicle.")
    def describe(self):
        print("This is a Vehicle.")
    def __str__(self):
        return f"{self.__class__.__name__} ({self.brand})"

#First level subclasses (Car, Train)

class Car(Vehicle):

    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def describe(self):
        print("This is a car.")
    
    def hello(self):
        print("Hello from Car")

    def __str__(self):
        return super().__str__() + f" {self.model}"

class Train(Vehicle):
    def hello(self):
        print("Hello from Train")

    def describe(self):
        print("This is a Train.")


# Car subclasses (Cabrio, SUV, Combi)

class Cabrio(Car):
    def describe(self):
        print("Cabrio with a retractable roof.")

class Combi(Car):
    def describe(self):
        print("Combi with extended space")

class SUV(Car):
    def describe(self):
        print("SUV for rough terrain")



#Polymorphisim
vehicles = [Cabrio("BMW",2007), Combi("Skoda",2020), SUV("Toyota",2015), Train("Siemens")]

for v in vehicles:
    print(v)
    v.describe()
    v.hello()

