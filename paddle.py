from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()

        ### --- PADDLES SETUP --- ###
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid= 5, stretch_len=1 )
        self.penup()
        self.goto(position)
        self.is_moving_up = False
        self.is_moving_down = False


    ### --- PADDLES KEY PRESSES & RELEASES --- ###
    def start_up(self):
        self.is_moving_up = True
        self.is_moving_down = False  # Ensure opposite movement is stopped

    def stop_up(self):
        self.is_moving_up = False

    def start_down(self):
        self.is_moving_down = True
        self.is_moving_up = False  # Ensure opposite movement is stopped

    def stop_down(self):
        self.is_moving_down = False

    def update(self):
        # Called in the main game loop
        if self.is_moving_up:
            new_y = self.ycor() + 20  # 20 is the move distance
            self.goto(self.xcor(), new_y)
        elif self.is_moving_down:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)








    # ### --- MOVING PADDLES--- ###
    # # Functions to call for going UP & DOWN for the paddle
    # def go_up(self):
    #     new_y = self.ycor() + 20
    #     self.goto(self.xcor(), new_y)
    #
    # def go_down(self):
    #     new_y = self.ycor() - 20
    #     self.goto(self.xcor(), new_y)
