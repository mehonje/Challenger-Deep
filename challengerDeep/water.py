from sprite import Sprite
import pygame

class Water(Sprite):
    def __init__(self, gameEngine, costume):
        super().__init__(gameEngine, costume)

    def paint(self):
        if self.gameEngine.camY > -180:
            self.y = -180 - self.gameEngine.camY
        else:
            self.y = 0

        self.stamp(62.5, 100)
        pygame.draw.line(self.screen, (102, 175, 255),self. convertCoords(-240, 0 - self.gameEngine.camY, ""), self.convertCoords(240, 0 - self.gameEngine.camY, ""), width=1)
