import colorgram
import turtle
from turtle import Turtle, Screen
import random


Tim = Turtle()
Tim.shape("turtle")
Tim.color("green", "mediumblue")
Tim.pensize(2)
Tim.speed("fastest")
turtle.colormode(255)
Tim.penup()
Tim.setpos(-300,-300)
Tim.hideturtle()

def random_color():
    color = random.choice(color_list)
    return color


def draw_a_dotted_line():
    for _ in range(9):
        Tim.dot(20)
        Tim.fd(50)
        Tim.pencolor(random_color())
        Tim.dot(20)


def repositionFL():
    Tim.left(90)
    Tim.fd(50)
    Tim.left(90)


def repositionFR():
    Tim.right(90)
    Tim.fd(50)
    Tim.right(90)

color_list = [(225, 158, 58), (240, 41, 115), (136, 27, 62), (248, 229, 63), (240, 63, 45), (180, 36, 96), (24, 142, 72), (56, 203, 236), (34, 133, 202), (28, 174, 134), (134, 204, 86), (75, 20, 72), (181, 162, 52), (208, 133, 165), (200, 55, 37), (238, 163, 192)]

for _ in range(5):
    draw_a_dotted_line()
    repositionFL()
    draw_a_dotted_line()
    repositionFR()


screen = Screen()
screen.exitonclick()


# colors = colorgram.extract("painting.jpg", 20)
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

color_list = [(225, 158, 58), (240, 41, 115), (136, 27, 62), (248, 229, 63), (240, 63, 45), (180, 36, 96), (24, 142, 72), (56, 203, 236), (34, 133, 202), (28, 174, 134), (134, 204, 86), (75, 20, 72), (181, 162, 52), (208, 133, 165), (200, 55, 37), (238, 163, 192)]
