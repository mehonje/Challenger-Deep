import sys
import pygame
from timers import Timers
from player import Player
from sky import Sky
from water import Water
from ground import Ground
from ballast import Ballast
from light import Light
from particles import Particles
from textEngine import TextEngine
from soundEffects import SoundEffects
from music import Music

class gameEngine:
    def __init__(self, gameName):
        pygame.init()
        print(f"Thanks for playing {gameName}!")
        print("You can find me at https://scratch.mit.edu/users/mehonje/ and https://github.com/mehonje")
        print("This game was made using Mehonje's Game Engine - https://github.com/mehonje/Mehonje-s-Game-Engine")
        self.clock = pygame.time.Clock()
        tmp = pygame.display.Info()
        if tmp.current_h < tmp.current_w:
            self.width = (tmp.current_h - 60) * (4/3)
            self.height = tmp.current_h - 60
        else:
            self.width = tmp.current_w - 60
            self.height = (tmp.current_w - 60) * 0.75
        self.screen = pygame.display.set_mode((int(self.width), int(self.height)))
        pygame.display.set_caption(gameName)
        pygame.mixer.init()

        self.playerY = 0
        self.camY = 0
        self.playerDepth = 0
        self.ballastEnabled = 1

        self.setup()

    def setup(self):
        self.keys = pygame.key.get_pressed()
        self.timers = Timers(self, "")
        pygame.mixer.init()

        self.player = Player(self, "")
        self.sky = Sky(self, "sky.png")
        self.water = Water(self, "water.png")
        self.ground = Ground(self, "ground.png")
        self.ballast = Ballast(self, "ballast.png")
        self.light = Light(self, "light2.png")
        self.particles = Particles(self, "")
        self.textEngine = TextEngine(self, "")
        self.soundEffects = SoundEffects(self)
        self.music = Music(self, "")

    def runGame(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.tick()
            self.paint()

        pygame.quit()
        sys.exit()

    def tick(self):
        self.keys = pygame.key.get_pressed()

        self.timers.tick()
        self.soundEffects.tick()
        self.music.tick()
        self.player.tick()
        self.particles.tick()
        self.ballast.tick()
        self.light.tick()

        self.clock.tick(30)

    def paint(self):
        self.screen.fill((0, 1, 31))

        self.sky.paint()
        self.ground.paint()
        self.ballast.paint()
        self.particles.paintBubbles()
        self.player.paint()
        self.water.paint()
        self.light.paint()
        self.particles.paintGlow()
        self.music.paint()
        self.textEngine.paint()

        pygame.display.flip()

if __name__ == "__main__":
    game = gameEngine("Challenger Deep")
    game.runGame()
