from vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, brand, model, price, doors):
        Vehicle.__init__(self, brand, model, price)
        self.doors = doors

    def __str__(self):
        return "Marca: %s // Modelo: %s // Puertas: %s // Precio: %s" % (
            self.brand, self.model, self.doors, self.format_price())
