class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model
    def car_method(self):
        print("Car Method")

class Audi(Car):
    def __init__(self, color, model):
        print("Audi Constructor")
        super().__init__(color, model)
    def audi_method(self):
        print("Audi Method")

audi = Audi("Black", "A6")
audi.car_method()
audi.audi_method()
print(audi.color)
print(audi.model)