from turtle import Turtle

ALIGMENT = "center"
FONT_1 = ("Courier", 18, "bold")
FONT_2 = ("Courier", 48, "bold")

class Score(Turtle):

    def __init__(self, screensize, shape = "classic", undobuffersize = 1000, visible = False):
        super().__init__(shape, undobuffersize, visible)
        self.level = 1
        self.color("black")
        self.hideturtle()
        self.teleport(x=-screensize/2+70, y=screensize/2-25)
        self.refresh_score()

    def increase_level(self):
        self.level += 1
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.write(arg=f"Level: {self.level}",  align=ALIGMENT, font=FONT_1)
    
    def game_over(self):
        self.teleport(0,0)
        self.color("red")
        self.write(arg="GAME OVER",  align=ALIGMENT, font=FONT_2)
