#IMPORTS
from turtle import Screen
from paddle import Paddle
from score import Score
from bricks import Brick
import time

#WINDOW SETUP
window = Screen()
window.setup(1000, 600)
window.bgcolor('black')
window.title('Bricks Falling Game !')
window.tracer(0)

#OBJECTS SETUP
paddle = Paddle()
score = Score()
brick = Brick()

def make_game_false():
    global game
    game = False
    
#WINDOW LISTENING
window.listen()
window.onkey(paddle.right, "Right")
window.onkey(paddle.left, "Left")
window.onkey(make_game_false, 'Escape')

speed = 0.1
game = True
while game:
    window.update()
    time.sleep(speed)

    #CHECK IF IT HAVE REACHED THE END
    if not brick.ycor() <= -300:
        brick.fall()
        if brick.ycor() == -300:
            brick.clear()
            brick.create()
        
    #CHECK IF BRICKS TOUCHED THE PADDLE
    if (brick.ycor() <= -250 and brick.distance(paddle) <= 50):
        shape = brick.shape()
        color = brick.color()[0]
        
        #POINTS COUNTING
        if shape == 'turtle':
            if color == 'white':
                score.game_over()
                game = False
                
            else:
                score.increase(5)
                speed *= 0.8
                
        elif shape == 'triangle':
            score.reset_score()
            speed = 0.1
            
        elif shape == 'circle':
            score.increase(1)
            speed *= 0.8
    
        else:
            score.increase(2)
            speed *= 0.8
    
        brick.clear()
        brick.create()
        
window.exitonclick()