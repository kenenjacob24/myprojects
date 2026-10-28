class Vehicle:
    def __init__(self, seating_Capacity):
        self.seating_Capacity = seating_Capacity

    def fare(self):
        return self.seating_Capacity * 100

class Bus(Vehicle):
    def fare(self):
        total = super().fare()
        return total + total * 0.10

bus = Bus(50)
print("Total Bus fare is:", bus.fare())