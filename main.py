from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

display = Screen()
# screen setup
display.setup(width=600, height=600)
display.title("the snake game")
display.bgcolor("black")
display.tracer(0)

snake = Snake(3)
food = Food()
scoreboard = Scoreboard()

display.listen()
display.onkey(snake.up, "Up")
display.onkey(snake.down, "Down")
display.onkey(snake.left, "Left")
display.onkey(snake.right, "Right")
game_is_on = True
while game_is_on:
    snake.snake_movement(snake.snake_segments)
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increment_score()

    if snake.head.xcor() > 270 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -270:
        scoreboard.reset_score()
        snake.snake_reset()

    for segments in snake.snake_segments[1:]:
        if snake.head.distance(segments) < 10:
            scoreboard.reset_score()
            snake.snake_reset()

    time.sleep(0.1)
    display.update()
#
display.exitonclick()
