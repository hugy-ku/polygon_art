import turtle
import random

def draw_polygon(num_sides, size, orientation, location, color, border_size):
    turtle.penup()
    turtle.goto(location[0], location[1])
    turtle.setheading(orientation)
    turtle.color(color)
    turtle.pensize(border_size)
    turtle.pendown()
    for _ in range(num_sides):
        turtle.forward(size)
        turtle.left(360/num_sides)
    turtle.penup()

def get_new_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


# draw a polygon at a random location, orientation, color, and border line thickness
def random_polygon(sides, reductions=0):
    reduction = 0.618
    num_sides = sides
    size = random.randint(50, 150)
    orientation = random.randint(0, 90)
    location = [random.randint(-300, 300), random.randint(-200, 200)]
    color = get_new_color()
    border_size = random.randint(1, 10)
    draw_polygon(num_sides, size, orientation, location, color, border_size)

    # reduction
    for _ in range(reductions):
        turtle.penup()
        turtle.forward(size*(1-reduction)/2)
        turtle.left(90)
        turtle.forward(size*(1-reduction)/2)
        turtle.right(90)
        location[0] = turtle.pos()[0]
        location[1] = turtle.pos()[1]
        size *= reduction
        draw_polygon(num_sides, size, orientation, location, color, border_size)


inputs = {
    "1": lambda: random_polygon(3),
    "2": lambda: random_polygon(4),
    "3": lambda: random_polygon(5),
    "4": lambda: random_polygon(random.randint(3, 5)),
    "5": lambda: random_polygon(3, 2),
    "6": lambda: random_polygon(4, 2),
    "7": lambda: random_polygon(5, 2),
    "8": lambda: random_polygon(random.randint(3, 5), 2),
    "9": lambda: random_polygon(random.randint(3, 5), random.randint(0, 2)),
}

result = input("Which art do you want to generate? Enter a number between 1 to 9 inclusive: ")

turtle.speed(0)
turtle.bgcolor('black')
turtle.tracer(0)
turtle.colormode(255)

result_function = inputs[result]
for i in range(random.randrange(20, 30)):
    result_function()

turtle.done()
