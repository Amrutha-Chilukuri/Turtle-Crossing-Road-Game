from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.level = 1
        self.goto(-230, 250)
        self.write(f" Level: {self.level}", align="center", font=("Courier", 15, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", align="center", font=("Courier", 50, "normal"))

    def level_up(self):
        self.level += 1
        self.clear()
        self.goto(-230, 250)
        self.write(f" Level: {self.level}", align="center", font=("Courier", 15, "normal"))



