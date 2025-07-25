from sprite import Sprite
import pygame
from random import uniform

class Glow(Sprite):
    def __init__(self, gameEngine, x, y, size, costume = None):
        super().__init__(gameEngine, costume)
        self.glowX = x
        self.glowY = y
        self.size = size

    def tick(self):
            if self.gameEngine.playerDepth > 200 and abs(self.glowY - self.gameEngine.camY) > 185:
                self.glowX = uniform(-240, 240)
                self.glowY = self.gameEngine.camY + ((185 * (abs(self.gameEngine.player.yVelocity) / self.gameEngine.player.yVelocity)) + uniform(-2.5, 2.5))


    def paint(self):
        self.x, self.y = self.glowX, self.glowY - self.gameEngine.camY
        pygame.draw.circle(self.screen, (102, 175, 255), self.convertCoords(self.x, self.y), (self.size * (self.gameEngine.width / 480)), 0)
