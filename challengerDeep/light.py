from sprite import Sprite
import pygame

class Light(Sprite):
    def __init__(self, gameEngine, costume):
        super().__init__(gameEngine, costume)
        self.lightDir = 90
        self.lightSetting = 0

    def tick(self):
        self.lightDir += self.gameEngine.keys[pygame.K_d] or self.gameEngine.keys[pygame.K_RIGHT]
        self.lightDir -= self.gameEngine.keys[pygame.K_a] or self.gameEngine.keys[pygame.K_LEFT]
        if (self.gameEngine.keys[pygame.K_UP] + self.gameEngine.keys[pygame.K_DOWN] != 0) and (self.gameEngine.timers.timers[1] > 10):
            self.lightSetting += self.gameEngine.keys[pygame.K_UP] + self.gameEngine.keys[pygame.K_DOWN]
            self.lightSetting = self.lightSetting % 3
            self.gameEngine.timers.timers[1] = 0

    def paint(self):
        self.y = (self.gameEngine.playerY - 15) - self.gameEngine.camY
        self.dir = self.lightDir
        self.setCostume(f"light{self.lightSetting}.png")
        self.stamp(100 - (0.0025 * (self.gameEngine.playerDepth ** 2)), 100)
