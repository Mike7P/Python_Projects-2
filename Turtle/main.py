import turtle
from turtle import Turtle, Screen
import random

turns = [0, 90, 180, 270]
colors = ["red", 'green', 'blue', 'yellow', 'purple', 'orange', 'black']
Tim = Turtle()
Tim.shape("turtle")
Tim.color("green", "mediumblue")
Tim.pensize(2)
Tim.speed("fastest")
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(angle, radius):
    reps = int(360 / angle)
    for _ in range(reps):
        Tim.color(random_color())
        Tim.circle(radius, extent=None, steps=None)
        Tim.right(angle)


draw_spirograph(10, 150)


# def random_walk():
#     for num in range(7000):
#         Tim.color(random_color())
#         Tim.forward(30)
#         Tim.right(random.randint(1,360)


def random_walk():
    for _ in range(7000):
        Tim.color(random_color())
        Tim.forward(30)
        Tim.setheading(random.choice(turns))


# random_walk()

#
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         Tim.forward(100)
#         Tim.right(angle)
#
#
# def move():
#         Tim.penup()
#         Tim.left(90)
#         Tim.forward(325)
#         Tim.pendown()
#         Tim.right(90)
#
# move()
#
# for shape_side_n in range(3, 23):
#     Tim.color(random.choice(colors))
#     draw_shape(shape_side_n)


screen = Screen()
screen.exitonclick()
