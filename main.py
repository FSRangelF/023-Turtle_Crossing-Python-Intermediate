from turtle import Screen
from turtleX import TurtleX
from car import Car
from scoreboard import Score
import image_lib
import random
import time

SCREENSIZE = 600
DELAY = 0.09
MOVE_STEP = 50
CARS_PER_LEVEL = 5
SPEED_PER_LEVEL = 5
avg_car_speed = 20
game_over = False

# setup screen
screen = Screen()
screen.setup(width=SCREENSIZE, height=SCREENSIZE)
screen.bgcolor("white")
screen.bgpic(image_lib.BG_IMAGE)
screen.title("Turtle Crossing")
screen.tracer(0)

# register shape images
for item in image_lib.SHAPES:
    screen.register_shape(item['name'], item['path'])

# initialize main objects
turtle = TurtleX(default_step=MOVE_STEP, screen_size_y=SCREENSIZE)
score = Score(screensize=SCREENSIZE)
cars = Car(default_step=avg_car_speed, screen_size_x=SCREENSIZE)

# Control direction
screen.listen()
screen.onkeypress(key="space", fun=turtle.move_up)

while not game_over:
    screen.update()
    cars.move()

    # detect level up
    if turtle.ycor() >= SCREENSIZE/2 - 20:
        score.increase_level()
        turtle.reset_pos()
        cars.reset(CARS_PER_LEVEL)
        avg_car_speed += SPEED_PER_LEVEL

    # detect car at end of the road
    for car in cars.cars:
        if car.xcor() < -SCREENSIZE/2:
            car.teleport(x=SCREENSIZE/2, y=random.choice(cars.lanes))

    # detect colision between cars
    counter_i =0
    for car1 in cars.cars:
        counter_j = 0
        for car2 in cars.cars:
            if car1.ycor() == car2.ycor() and car1.distance(car2) < 80:
                cars.speed[counter_i] = cars.speed[counter_j] 
                counter_j +=1
        counter_i += 1

    # detect car colision / game over condition
    for car in cars.cars:
        if -20 < car.xcor() < 20 and car.distance(turtle) < 25:
            score.game_over()
            game_over = True
    
    time.sleep(DELAY)

screen.exitonclick()