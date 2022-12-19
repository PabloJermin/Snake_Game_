from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

# setting up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Catch Me If You Can")


# creating the snake object
snake = Snake()
food = Food()
score = Score()


# listening to event
screen.listen()
screen.onkey(key = "Up", fun= snake.up)
screen.onkey(key = "Down", fun= snake.down)
screen.onkey(key = "Left", fun= snake.left)
screen.onkey(key = "Right", fun= snake.right)

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


#     detecting a hit with ball
    if snake.head.distance(food) < 15:
        food.refresh_food()
        snake.new_tail()
        score.new_score()

#     colition with wall
    if snake.head.xcor() > 288 or snake.head.xcor() < -288 or snake.head.ycor() > 288 or snake.head.ycor() < -288:
        game_on = False
        score.game_over()

    #     tail colition
    for touch_body in snake.snake_body[1:]:
        if snake.head.distance(touch_body) < 10:
            game_on = False
            score.game_over()






screen.exitonclick()