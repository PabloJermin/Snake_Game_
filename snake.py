from turtle import Turtle

# constant value
CORDINATES = [0, -20, -40]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        # creating a snake body
         self.add_new_tail()


    #     adding a tail
    def add_new_tail(self):
        for body in range(0, 2):
            new_body = Turtle()
            new_body.penup()
            new_body.shape("square")
            new_body.color("white")
            new_body.goto(x=CORDINATES[body], y=0)
            self.snake_body.append(new_body)

    def new_tail(self):
        self.add_new_tail()

    def move(self):
        for move in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[move - 1].xcor()
            new_y = self.snake_body[move - 1].ycor()
            self.snake_body[move].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)


    # setting the controls
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

