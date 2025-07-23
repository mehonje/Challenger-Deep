from sprite import Sprite
import pygame
from random import randint
import math

class Player(Sprite):
    def __init__(self, gameEngine, costume = None):
        super().__init__(gameEngine, costume)
        #set ship data
        if self.gameEngine.ship == 1:
            self.subVolume = 32.338
            self.subDragArea = 8.74
            self.subWeight = 12500
            self.ballastWeight = 21100

        else:
            self.subVolume = 31.671
            self.subDragArea = 3.91
            self.subWeight = 11800
            self.ballastWeight = 21100

        self.yVelocity = 0

    def tick(self):
        self.playerPhysics()
        self.gameEngine.playerY += self.yVelocity * self.gameEngine.timers.deltaTime
        self.boundPlayer()
        self.gameEngine.camY = self.gameEngine.playerY
        self.gameEngine.playerDepth = abs(self.gameEngine.playerY * 0.1)

    def paint(self):
        if self.gameEngine.ship == 1:
            self.setCostume("dsv limiting factor.png")
        else:
            self.setCostume("deepsea challenger.png")
        self.y = self.gameEngine.playerY - self.gameEngine.camY
        self.stamp(0, 100)

    def playerPhysics(self):
        self.addVerticalForce((self.gameEngine.keys[pygame.K_w] - self.gameEngine.keys[pygame.K_s]) * 10 * self.gameEngine.timers.deltaTime, 0)
        #gravity
        self.addVerticalForce(98.1 * self.gameEngine.timers.deltaTime, 180)
        #buoyancy
        self.addVerticalForce(((997 * self.subVolume * 9.81) / (self.subWeight + (self.ballastWeight * self.gameEngine.ballastEnabled))) * self.gameEngine.timers.deltaTime * 10, 0)
        self.addDragForce()

    def addDragForce(self):
        self.tmp1 = (0.5 * 997 * (self.yVelocity ** 2) * 0.75 * self.subDragArea) / (self.subWeight + (self.ballastWeight * self.gameEngine.ballastEnabled))
        if self.yVelocity > 0:
            self.addVerticalForce(self.tmp1 * self.gameEngine.timers.deltaTime, 180)
        else:
            self.addVerticalForce(self.tmp1 * self.gameEngine.timers.deltaTime, 0)

    def boundPlayer(self):
        if self.gameEngine.playerY > 0:
            self.gameEngine.playerY = 0
            self.yVelocity *= -0.9
        else:
            if self.gameEngine.ship == 0:
                if self.gameEngine.playerY < -109141.5:
                    self.gameEngine.playerY = -109141.5
                    self.yVelocity *= -0.9
            else:
                if self.gameEngine.playerY < -109119.5:
                    self.gameEngine.playerY = -109119.5
                    self.yVelocity *= -0.9

    def addVerticalForce(self, force, dir):
        self.yVelocity += math.cos(math.radians(dir)) * force
