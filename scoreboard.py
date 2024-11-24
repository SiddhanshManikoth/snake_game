from turtle import Turtle


class Scoreboard(Turtle):
    ALIGNMENT = "center"
    FONT = ("Arial", 10, "normal")

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        with open("data.txt") as data:
            self.high_score=data.read()
        self.penup()
        self.goto(0, 280)
        self.score = 0
        self.update_score()


    def reset_score(self):
        if self.score>int(self.high_score):
            self.high_score=self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.high_score))
        self.score=0
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(arg=f"SCORE:{self.score} highScore : {self.high_score}", align=self.ALIGNMENT, font=self.FONT)



    def increment_score(self):
        self.clear()
        self.score += 1
        self.update_score()
