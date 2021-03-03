import random
import turtle
from tkinter import *

wn = turtle.Screen()
wn.bgcolor("#2c78db")
wn.title("Dice SIM")

pen = turtle.Turtle()
pen.color("black")
pen.hideturtle()
pen.penup()
pen.goto(0, 120)

border_pen = turtle.Turtle()
border_pen.hideturtle()
border_pen.goto(-150, 0)
s = 300

for i in range(4):
    border_pen.forward(s)
    border_pen.left(90)

def roll_dice():
    number = random.randint(1, 6)
    pen.clear()
    pen.write(number, align="center", font=("Arial", 40, "bold"))

roll_button = Button(text="ROLL", command=roll_dice, height=5, width=40, bg="#bf6132")
roll_button.place(relx = 0.5, rely = 0.850, anchor = CENTER)

wn.mainloop()