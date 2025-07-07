from sprite import Sprite

class Sky(Sprite):
    def __init__(self, gameEngine, costume):
        super().__init__(gameEngine, costume)
        
    def paint(self):
        self.y = 0 - self.gameEngine.camY
        self.stamp(0, 100)