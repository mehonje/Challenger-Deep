from sprite import Sprite

class Ground(Sprite):
    def __init__(self, gameEngine, costume):
        super().__init__(gameEngine, costume)

    def paint(self):
        self.y = -109160 - self.gameEngine.camY
        self.stamp(0, 100)