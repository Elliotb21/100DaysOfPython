from turtle import Turtle, Screen

MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.snake_head = self.snake_body[0]
        
        
    def create_snake(self):
        for position in STARTING_POSITIONS:
            segment = Turtle("square")
            segment.penup()
            segment.color("white")
            segment.goto(position)
            self.snake_body.append(segment)


    def move(self):
        for segment in range(len(self.snake_body) -1 , 0, -1):
            new_x = self.snake_body[segment -1].xcor()
            new_y = self.snake_body[segment -1].ycor()
            self.snake_body[segment].goto(new_x, new_y)
        self.snake_body[0].forward(MOVE_DISTANCE)    


    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)
        
    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)
        
    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)
        