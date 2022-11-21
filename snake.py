from turtle import Turtle

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

speed = 10


class Snake:
    snake = []
    angle = 0

    def __init__(self, initial_length):
        self.INITIAL_SNAKE_LENGTH = initial_length
        self.distance = 20

    def create_snake(self):
        x_cor = 0
        for _ in range(0, self.INITIAL_SNAKE_LENGTH):
            new_square = Turtle("square")
            new_square.penup()
            new_square.goto(x_cor, 0)
            new_square.color("white")
            self.snake.append(new_square)
            x_cor -= 20
        self.angle = self.snake[0].heading()

    def move(self):
        for square_number in range(len(self.snake) - 1, 0, -1):
            x_cor = self.snake[square_number - 1].xcor()
            y_cor = self.snake[square_number - 1].ycor()
            self.snake[square_number].goto(x_cor, y_cor)
        self.snake[0].setheading(self.angle)
        self.snake[0].forward(self.distance)

    def up(self):
        if self.angle != DOWN:
            self.angle = UP

    def down(self):
        if self.angle != UP:
            self.angle = DOWN

    def right(self):
        if self.angle != LEFT:
            self.angle = RIGHT

    def left(self):
        if self.angle != RIGHT:
            self.angle = LEFT

    def grow_snake(self):
        new_square = Turtle("square")
        new_square.penup()
        new_square.color("white")
        x_cor = self.snake[-1].xcor()
        y_cor = self.snake[-1].ycor()
        if self.angle == UP:
            new_square.goto(x_cor, y_cor-20)
        elif self.angle == DOWN:
            new_square.goto(x_cor, y_cor + 20)
        elif self.angle == LEFT:
            new_square.goto(x_cor + 20, y_cor)
        elif self.angle == RIGHT:
            new_square.goto(x_cor + 20, y_cor)
        self.snake.append(new_square)

    def reset(self):
        for square in self.snake:
            square.goto(2000, 2000)
        self.snake.clear()
        self.create_snake()
