from turtle import Turtle

ALIGMENT = 'center'
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color('white')
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score}   High score: {self.high_score}', align=ALIGMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write('GAME OVER', align=ALIGMENT, font=FONT)