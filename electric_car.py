from car import Car


class ElectricCar(Car):
    def __init__(self, brand, model, price, doors, voltage):
        Car.__init__(self, brand, model, price, doors)
        self.voltage = voltage

    def __str__(self):
        return super(ElectricCar, self).__str__() + " // Voltaje: %s" % self.voltage

    def is_luxury(self):
        return True
