class Vehicle:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def format_price(self):
        return "$" + str(self.price)

    def short_str(self):
        return self.brand + " " + self.model

    def is_luxury(self):
        return False
