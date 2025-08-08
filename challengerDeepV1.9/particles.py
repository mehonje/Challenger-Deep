from sprite import Sprite
from bubble import Bubble
from glow import Glow
import pygame

from random import uniform

class Particles(Sprite):
    def __init__(self, gameEngine, costume = None):
        super().__init__(gameEngine, costume)
        self.bubbles = []
        self.glow = []

        for x in range(25):
            self.newParticle = Glow(self.gameEngine, uniform(-240, 240), uniform(-1820, -2180), uniform(1.0, 2.0))
            self.glow.append(self.newParticle)

    def tick(self):
        tmp = self.gameEngine.keys[pygame.K_w] - self.gameEngine.keys[pygame.K_s]
        if tmp != 0:
            if self.gameEngine.ship == 1:
                newParticle = Bubble(self.gameEngine, uniform(-19.9, -20.1), self.gameEngine.playerY, uniform(-0.1, 0.1), uniform(-0.1, 0.1), uniform(2.0, 3.0))
                self.bubbles.append(newParticle)
                newParticle = Bubble(self.gameEngine, uniform(19.9, 20.1), self.gameEngine.playerY, uniform(-0.1, 0.1), uniform(-0.1, 0.1), uniform(2.0, 3.0))
                self.bubbles.append(newParticle)
            else:
                newParticle = Bubble(self.gameEngine, uniform(-9.9, -9.1), self.gameEngine.playerY - 6, uniform(-0.1, 0.1), uniform(-0.1, 0.1), uniform(2.0, 3.0))
                self.bubbles.append(newParticle)
                newParticle = Bubble(self.gameEngine, uniform(9.1, 9.9), self.gameEngine.playerY - 6, uniform(-0.1, 0.1), uniform(-0.1, 0.1), uniform(2.0, 3.0))
                self.bubbles.append(newParticle)
            
        self.bubblesCopy = self.bubbles
        for particle in self.bubblesCopy:
            particle.tick()
            if (particle.bubbleY > 0) or (particle.bubbleY > self.gameEngine.playerY + 180) or (particle.bubbleY < self.gameEngine.playerY - 180):
                self.bubbles.remove(particle)

        for particle in self.glow:
            particle.tick()

    def paintBubbles(self):
        for particle in self.bubbles:
            particle.paint()

    def paintGlow(self):
        for particle in self.glow:
            particle.paint()
