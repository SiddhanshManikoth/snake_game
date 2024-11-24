from turtle import Turtle

move_distance = 20


class Snake:
    def __init__(self, length):
        self.snake_segments = self.body_gen(3)
        self.head = self.snake_segments[0]
        self.head.color("green")

    def body_gen(self, no_of_segments):
        SnakeBody = []
        for i in range(no_of_segments):
            pos = (-(i * 20), 0)
            SnakeBody.append(self.add(pos))

        return SnakeBody

    def add(self, position):

        new_turtle = Turtle()
        new_turtle.hideturtle()
        new_turtle.color("white")
        new_turtle.shape("square")
        new_turtle.penup()
        new_turtle.speed(0)
        new_turtle.goto(position)
        new_turtle.showturtle()

        return new_turtle

    def extend(self):
        self.snake_segments.append(self.add(self.snake_segments[-1].position()))

    def snake_movement(self, snake_body):
        for new_seg in range(len(snake_body) - 1, 0, -1):
            newX = snake_body[new_seg - 1].xcor()
            newY = snake_body[new_seg - 1].ycor()
            snake_body[new_seg].goto(newX, newY)
        snake_body[0].fd(move_distance)
        return snake_body

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def snake_reset(self):
        for segment in self.snake_segments:
            segment.goto(1000, 1000)
        self.snake_segments.clear()
        self.snake_segments = self.body_gen(3)
        self.head = self.snake_segments[0]
        self.head.color("green")
