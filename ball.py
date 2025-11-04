from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()


    ### --- BALL SETUP --- ###
        self.shape("circle")
        self.color("coral")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_spd = 0.1


    ### --- BALL MOVEMENT --- ###
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)


    ### --- BALL BOUNCE FROM TOP & BOTTOM WALLS --- ###
    def bounce_y(self):
        # Once the ball reaches both the top and bottom wall coordinates,
        # the ball will reverse direction in the y direction
        self.y_move *= -1


    ### --- BALL BOUNCE FROM PADDLES --- ###
    def bounce_x(self):
        # Once the ball hit the paddle,
        # the ball will reverse direction in the x direction
        self.x_move *= -1
        self.move_spd *= 0.9


    ### --- BALL RESET POSITION --- ###
    def reset_position(self):
        self.goto(0, 0)
        self.move_spd = 0.1
        self.bounce_x()





