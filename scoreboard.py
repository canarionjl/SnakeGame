from turtle import Turtle

FONT = ('Arial', 16, 'bold')
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 275)
        self.score = 0
        with open(file="high_score.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} - Highest Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(file="high_score.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)
