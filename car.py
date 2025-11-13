from turtle import Turtle
import random
import image_lib

CAR_INITIAL_N = 10

class Car:
    
    def __init__(self, default_step, screen_size_x):
        self.screensize = screen_size_x
        self.step = default_step
        self.cars = []
        self.lanes = []
        self.speed = []
        self.shapes = []
        self.initial_def()
        self.reset(CAR_INITIAL_N)

    def move(self):
        index = 0
        for car in self.cars:
            car.backward(self.speed[index])
            index += 1

    def initial_def(self):
        size = self.screensize/2 - 50
        for i in range (0, int((self.screensize-100)/50)):
            size -= 25
            self.lanes.append(size)
            size -= 25
        for i in range(1, len(image_lib.SHAPES)):
            self.shapes.append(image_lib.SHAPES[i]['name'])

    def reset(self, list_increase):
        for car in self.cars:
            car.teleport(x=random.randint(int(self.screensize/2), int(1.5*self.screensize)), y=random.choice(self.lanes))
        for i in range(0, list_increase):
            car = Turtle()
            car.shape(random.choice(self.shapes))
            car.penup()
            car.shapesize(stretch_len=2, stretch_wid=3)
            car.teleport(x=random.randint(int(self.screensize/2), int(1.5*self.screensize)), y=random.choice(self.lanes))
            self.cars.append(car)
            self.speed.append(random.randint(int(self.step*0.5), int(1.5*self.step)))
        print(list_increase)