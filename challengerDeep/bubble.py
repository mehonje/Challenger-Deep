from sprite import Sprite
import pygame

class Bubble(Sprite):
    def __init__(self, gameEngine, costume, x, y, xVelocity, yVelocity, size):
        super().__init__(gameEngine, costume)
        self.bubbleX = x
        self.bubbleY = y
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity
        self.size = size

    def tick(self):
        self.bubbleX += self.xVelocity
        self.bubbleY += self.yVelocity
        self.xVelocity *= 0.99
        self.yVelocity += self.gameEngine.timers.deltaTime
        self.yVelocity *= 0.9

    def paint(self):
        self.x, self.y = self.bubbleX, self.bubbleY - self.gameEngine.camY
        pygame.draw.circle(self.screen, (102, 175, 255), self.convertCoords(self.x, self.y), (self.size / 2 * (self.gameEngine.width / 480)), 0)
