class BMW:
    def fuel_type(self):
        print("BMW uses Petrol")
    def max_speed(self):
        print("BMW has a maximum speed of 250 km/h")

class Audi:
    def fuel_type(self):
        print("Audi uses Diesel")
    def max_speed(self):
        print("Audi has a maximum speed of 240 km/h")

car1 = BMW()
car2 = Audi()

for car in (car1, car2):
    car.fuel_type()
    car.max_speed()
    