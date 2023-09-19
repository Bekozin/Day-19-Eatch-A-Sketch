import random
from turtle import Turtle, Screen

l = []
colors = ["chocolate", "cyan", "DarkGrey", "blue", "gray"]
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")

turtle1 = Turtle()
turtle2 = Turtle()
turtle3 = Turtle()
turtle4 = Turtle()
turtle5 = Turtle()

while colors != l:
    turtle5.color(user_bet)
    colors.remove(user_bet)

    x = random.choice(colors)
    turtle1.color(x)
    colors.remove(x)

    y = random.choice(colors)
    turtle2.color(y)
    colors.remove(y)

    z = random.choice(colors)
    turtle3.color(z)
    colors.remove(z)

    k = random.choice(colors)
    turtle4.color(k)
    colors.remove(k)

# initial positions

turtle1.penup()
turtle1.goto(x=-250, y=0)

turtle2.penup()
turtle2.goto(x=-250, y=50)

turtle3.penup()
turtle3.goto(x=-250, y=-50)

turtle4.penup()
turtle4.goto(x=-250, y=100)

turtle5.penup()
turtle5.goto(x=-250, y=-100)

screen.exitonclick()
