from turtle import Turtle

FONT = ("arial", 10, "normal")


class Label(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def create_label(self, x, y, state_name):
        self.goto(x, y)
        self.write(state_name, align="center", font=FONT)