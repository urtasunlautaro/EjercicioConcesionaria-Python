from car import Car
from motorcycle import Motorcycle
from operator import attrgetter


class VehicleDealer:

    def __init__(self):
        self.vehicles = self.init_vehicles()

    def init_vehicles(self):
        peugeot_206 = Car("Peugeot", "206", 200000.00, 4)
        honda_titan = Motorcycle("Honda", "Titan", 60000.00, "125c")
        peugeot_208 = Car("Peugeot", "208", 250000.00, 5)
        yamaha_ybr = Motorcycle("Yamaha", "YBR", 80500.50, "160c")
        return [peugeot_206, honda_titan, peugeot_208, yamaha_ybr]

    def print_vehicles(self):
        for vehicle in self.vehicles:
            print(vehicle.__str__())

    def print_most_expensive(self):
        self.price_sort(True)
        most_expensive = self.vehicles[0]
        print("Vehículo más caro: " + most_expensive.short_str())

    def print_least_expensive(self):
        self.price_sort(False)
        least_expensive = self.vehicles[0]
        print("Vehículo más barato: " + least_expensive.short_str())

    def print_sorted_by_price(self):
        print("Vehículos ordenados por precio de mayor a menor")
        self.price_sort(True)
        for vehicle in self.vehicles:
            print(vehicle.short_str())

    def print_containing_letter(self, letter):
        contains_letter = []
        for vehicle in self.vehicles:
            if vehicle.model.find(letter) == 0:
                contains_letter.append(vehicle)
        print("Vehículos que contienen en el modelo la letra 'Y': ")
        for vehicle in contains_letter:
            print("-" + vehicle.short_str())

    def price_sort(self, do_reverse):
        self.vehicles.sort(reverse=do_reverse, key=attrgetter("price"))

    def print_line_separator(self):
        print("=============================")

    def print_catalog(self):
        self.print_most_expensive()
        self.print_least_expensive()
        self.print_containing_letter("Y")
        self.print_line_separator()
        self.print_sorted_by_price()
