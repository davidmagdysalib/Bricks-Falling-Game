from turtle import Turtle

class Paddle(Turtle):
    """
    The Paddle Class That Inherits From Turtle Class From turtle module

    Args:
        Turtle (_type_): _description_
    """
    
    def __init__(self):
        """
        Initialize Magic Method
        """
        
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(1, 5)
        self.goto(0, -270)
        
    def right(self):
        """
        Go Right
        """
        
        if not self.xcor() >= 450:
            self.goto(self.xcor()+20, self.ycor())
            
    def left(self):
        """
        Go Left
        """
        
        if not self.xcor() <= -450:
            self.goto(self.xcor()-20, self.ycor())