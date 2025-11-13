from turtle import Turtle

class TurtleX(Turtle):
    
    def __init__(self, default_step, screen_size_y, shape = "turtlex", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.init_y = -screen_size_y/2 + 25
        self.step = default_step
        self.penup()
        self.shapesize(stretch_len=2.5, stretch_wid=2.5)
        self.teleport(x=0, y= self.init_y)
        self.setheading(90)

    def move_up(self):
        self.forward(self.step)

    def reset_pos(self):
        self.teleport(x=0, y= self.init_y)
