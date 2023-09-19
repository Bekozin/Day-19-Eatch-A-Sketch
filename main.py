import random
from turtle import Turtle, Screen

l = []
colors = ["chocolate", "cyan", "DarkGrey", "blue", "gray"]
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")
y_initials = [-100, -50, 0, 50, 100]
competitor_list = []
is_race_on = False

for turtle_index in range(0, 5):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-250, y=y_initials[turtle_index])
    competitor_list.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in competitor_list:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is winner.")

            else:
                print(f"You've lost! The {winning_color} turtle is winner")

        rand_distance = random.randint(1, 20)
        turtle.forward(rand_distance)

screen.exitonclick()
