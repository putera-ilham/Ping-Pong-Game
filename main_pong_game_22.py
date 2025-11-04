import time
from turtle import Turtle, Screen
from paddle import  Paddle
from ball import Ball
from scoreboard import Scoreboard

### --- SCREEN SETUP --- ###
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONGERS")
screen.tracer(0)


### --- INITIALISING THE OBJECTS--- ###
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()


### --- INITIALISING THE KEYS FOR THE PADDLES TO MOVE --- ###
screen.listen()

### --- KEY PRESSES & RELEASES FOR THE RIGHT PADDLE TO MOVE --- ###
screen.onkeypress(r_paddle.start_up, "Up")
screen.onkeyrelease(r_paddle.stop_up, "Up")
screen.onkeypress(r_paddle.start_down, "Down")
screen.onkeyrelease(r_paddle.stop_down, "Down")

### --- KEY PRESSES & RELEASES FOR THE LEFT PADDLE TO MOVE --- ###
screen.onkeypress(l_paddle.start_up, "w")
screen.onkeyrelease(l_paddle.stop_up, "w")
screen.onkeypress(l_paddle.start_down, "s")
screen.onkeyrelease(l_paddle.stop_down, "s")


### --- WHILE LOOP FOR GAME RUN SETUP --- ###
game_on = True
while game_on:
    time.sleep(ball.move_spd)
    screen.update()  # Update the screen graphics
    ball.move()

    # Call the update method on paddles to check their movement state
    r_paddle.update()
    l_paddle.update()


    ### --- COLLISION OF BALL WITH THE TOP & BOTTOM SCREEN --- ###
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    ### --- COLLISION OF BALL WITH BOTH PADDLES --- ###
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320 :
        ball.bounce_x()

    ### --- DETECTION OF RIGHT PADDLE MISS --- ###
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    ### --- DETECTION OF RIGHT PADDLE MISS --- ###
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()



### --- SCREEN EXIT --- ###
screen.exitonclick()


