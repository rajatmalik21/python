class Car:
    def __init__ (self,make,model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f'<Car {self.make} {self.model}'


class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def add_car(self,car):
        if not isinstance(car,Car):
            raise TypeError(f'Tried to add a `{car.__class__.__name__}` to the garage you can only add Car objects')
        #how to raise an error
        raise NotImplementedError ("This is a work in progress")


ford = Garage()
ford.add_car("Fiesta")
print(len(ford))