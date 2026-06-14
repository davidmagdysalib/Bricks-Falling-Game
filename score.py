from turtle import Turtle

class Score(Turtle):
    """
    The Score Class That Inherits From Turtle Class From turtle module

    Args:
        Turtle (_type_): _description_
    """
    
    def __init__(self):
        """
        Initialize Magic Method
        """
        
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0, 230)
        self.score = 0
        self.display()
        
    def display(self):
        """
        Display Method
        """
        
        self.write(f'Score : {self.score}', align= 'center', font= ("courier", 24, 'normal'))
        
    def increase(self, points):
        """
        Increase Points Based On Shape

        Args:
            points (_type_): _description_
        """
        self.score += points
        self.clear()
        self.display()
        
    def game_over(self):
        """
        Game Over Method
        """
        
        self.goto(0,0)
        self.clear()
        self.write(f'Game Over\nScore : {self.score}', align= 'center', font= ("courier", 24, 'normal'))
        
    def reset_score(self):
        """
        This Method Resets The Score
        """
        self.score = 0
        self.increase(0)