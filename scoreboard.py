from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.score_1 = 0
        self.score_2 = 0
        self.color("White")
        self.goto(0,270)
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f"Player 1: {self.score_1}  |  Player 2: {self.score_2}", align="center",
                   font=("Arial", 20, "normal"))
        self.hideturtle()