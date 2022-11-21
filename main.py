from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

INITIAL_TIME_DIFFICULTY = 0.2


def create_border_square():
    border_value = 270
    border = Turtle()
    border.color("white")
    border.penup()
    border.goto(-border_value, border_value)
    border.pendown()
    border.goto(border_value, border_value)
    border.goto(border_value, -border_value)
    border.goto(-border_value, -border_value)
    border.goto(-border_value, border_value)
    border.hideturtle()


def configure_screen():
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)
    scoreboard.update_score()
    create_border_square()


snake_object = Snake(3)
snake_object.create_snake()

food = Food()
scoreboard = Scoreboard()

screen = Screen()
configure_screen()

screen.listen()
screen.onkey(snake_object.up, "Up")
screen.onkey(snake_object.down, "Down")
screen.onkey(snake_object.right, "Right")
screen.onkey(snake_object.left, "Left")

game_is_on = True
time_difficulty = INITIAL_TIME_DIFFICULTY
while game_is_on:
    screen.update()
    time.sleep(time_difficulty)
    snake_object.move()

    # Detect collision with food
    if snake_object.snake[0].distance(food) < 15:
        time_difficulty *= 0.9
        scoreboard.increase_score()
        food.generate_location()
        snake_object.grow_snake()

    # Detect collision with wall
    x_cor = snake_object.snake[0].xcor()
    y_cor = snake_object.snake[0].ycor()
    if x_cor >= 280 or x_cor <= -280 or y_cor >= 280 or y_cor <= -280:
        # game_is_on = False
        scoreboard.reset()
        snake_object.reset()
        time_difficulty = INITIAL_TIME_DIFFICULTY

    # Detect collision with the body of the snake (tail)
    for square in snake_object.snake[1:]:
        if snake_object.snake[0].distance(square) < 10:
            # game_is_on = False
            scoreboard.reset()
            snake_object.reset()
            time_difficulty = INITIAL_TIME_DIFFICULTY

screen.exitonclick()
