class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r
    def perimeter(self):
        return 2 * 3.14 * self.r

r = float(input("Enter the radius of the circle: "))
c = Circle(r)
print("Area of the circle:", c.area())
print("Perimeter of the circle:", c.perimeter())

        