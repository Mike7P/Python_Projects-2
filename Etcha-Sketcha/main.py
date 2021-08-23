from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.fd(50)


def move_backwards():
    tim.back(50)

def move_left():
    tim.left(10)


def move_right():
    tim.right(10)

def clearing_screen():
    tim.clear()


def center():
    tim.home()
    tim.clear()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="space", fun=clearing_screen)
screen.onkey(key="g", fun=center)

screen.exitonclick()




