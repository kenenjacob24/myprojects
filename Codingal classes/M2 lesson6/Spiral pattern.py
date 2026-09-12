import turtle 
my_wn = turtle.Screen()
my_wn.bgcolor("light blue")
my_wn.title("Title")
my_pen = turtle.Turtle()
size = 0
while True:
    for i in range(7):
        my_pen.forward(size + 1)
        my_pen.left(30)
        size = size - 7
    size = size + 5