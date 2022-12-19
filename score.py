from turtle import Turtle
FONT = ("Courier", 19, "italic")
ALIGNMENT = "center"


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.scor = 0
        self.penup()
        self.color("white")
        self.goto(x=0, y=270)
        self.score_board()
        self.hideturtle()


    def score_board(self):
        self.write(f"Score: {self.scor} ", align=ALIGNMENT, font=FONT)


    def new_score(self):
        self.scor += 1
        self.clear()
        self.score_board()

    def game_over(self):
        self.clear()
        self.goto(x=0, y=0)
        self.write("Game Over", align="center", font=FONT)
        self.goto(x=0, y=-20)
        self.write(f"You scored: {self.scor}", align="center", font=FONT)


