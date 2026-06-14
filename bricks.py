from turtle import Turtle
import random

class Brick(Turtle):
    """
    The Bricks Class That Inherits From Turtle Class From turtle module

    Args:
        Turtle (_type_): _description_
    """
    
    def __init__(self):
        """
        Initialize Magic Method
        """
        
        super().__init__()
        self.shapes = ('square', 'circle', 'turtle', 'triangle')
        self.colors = ('green', 'blue', 'orange', 'yellow', 'purple', 'white', 'white', 'white', 'white')
        self.y = -10
        self.penup()
        self.create()
        
    def create(self):
        """
        The Method That Creates Bricks
        """
        
        self.goto(random.randint(-450, 450), 300)
        self.shape(random.choice(self.shapes))
        self.color(random.choice(self.colors))
        size = random.uniform(0.5, 2)
        self.shapesize(size, size)
        
    def fall(self):
        """
        The Method That Makes Bricks Falls
        """
        
        self.goto(self.xcor(), self.ycor()+self.y)
        