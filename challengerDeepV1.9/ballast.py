from sprite import Sprite
import pygame
import math

class Ballast(Sprite):
    def __init__(self, gameEngine, costume):
        super().__init__(gameEngine, costume)
        self.ballastY = 0
        self.yVelocity = 0

    def tick(self):
        if self.gameEngine.ballastEnabled == 1:
            self.ballastY = self.gameEngine.playerY - 14
            if self.gameEngine.keys[pygame.K_SPACE] == 1:
                self.gameEngine.ballastEnabled = 0
        else:
            #gravity
            self.addVerticalForce(98.1 * self.gameEngine.timers.deltaTime, 180)
            #drag
            if self.yVelocity > 0:
                self.addVerticalForce(((0.5 * (997 * ((self.yVelocity ** 2) * (1.05 * 64)))) / 21100) * self.gameEngine.timers.deltaTime, 180)
            else:
                self.addVerticalForce(((0.5 * (997 * ((self.yVelocity ** 2) * (1.05 * 64)))) / 21100) * self.gameEngine.timers.deltaTime, 0)
            #buoyancy
            self.addVerticalForce(((((997 * 9.81) * 0.512) / 21100) * 10) * self.gameEngine.timers.deltaTime, 0)
            
            if abs(self.yVelocity) > 25:
                self.yVelocity = 25 * math.copysign(1, self.yVelocity)

            self.ballastY += self.yVelocity * self.gameEngine.timers.deltaTime
            
            if self.ballastY < -109156:
                self.ballastY = -109156
                self.yVelocity *= -0.9

    def paint(self):
        self.y = self.ballastY - self.gameEngine.camY
        self.stamp(0, 100)

    def addVerticalForce(self, force, dir):
        self.yVelocity += math.cos(math.radians(dir)) * force