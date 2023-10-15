import turtle
from turtle import Turtle, Screen
# import colorgram
import random

# colors = colorgram.extract('img.jpg', 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
color_list = [(198, 13, 32), (250, 237, 19), (39, 76, 189), (39, 217, 68), (238, 227, 5), (229, 159, 47), (28, 40, 156),
              (214, 75, 13), (242, 246, 252), (16, 154, 16), (198, 15, 11), (243, 34, 165), (68, 10, 30),
              (228, 18, 120), (60, 15, 8), (223, 141, 209), (11, 97, 62), (221, 161, 9), (50, 212, 231), (18, 20, 47),
              (11, 227, 239), (238, 156, 217), (84, 74, 211), (78, 210, 163), (82, 234, 200), (61, 233, 241),
              (5, 68, 42)]

cursor = Turtle()
cursor.speed('fastest')
cursor.hideturtle()
cursor.penup()
turtle.colormode(255)
cursor.setheading(225)
cursor.forward(300)
cursor.setheading(0)
no_of_dots = 100
for dot in range(1, no_of_dots + 1):
    random_color = random.choice(color_list)
    cursor.dot(20, random_color)
    cursor.forward(50)
    if dot % 10 == 0:
        cursor.setheading(90)
        cursor.forward(50)
        cursor.setheading(180)
        cursor.forward(500)
        cursor.setheading(0)

screen = Screen()
screen.exitonclick()
