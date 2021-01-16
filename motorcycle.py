from vehicle import Vehicle


class Motorcycle(Vehicle):
    def __init__(self, brand, model, price, cilinders):
        Vehicle.__init__(self, brand, model, price)
        self.cilinders = cilinders

    def __str__(self):
        return "Marca: %s // Modelo: %s // Cilindrada: %sc // Precio: %s" % (
            self.brand, self.model, self.cilinders, self.format_price())

    def is_luxury(self):
        if self.cilinders > 150:
            return True
        else:
            return False
