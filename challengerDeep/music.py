from sprite import Sprite
import pygame
import random
import time

class Music(Sprite):
    def __init__(self, gameEngine, costume):
        super().__init__(gameEngine, costume)
        self.songs = ["songs/hammockTurnAwayAndReturn.mp3", "songs/scottBuckleyAurora.mp3", "songs/erikWernquistCassini'sGrandFinale.mp3", "songs/cristianSandquistWanderers.mp3", "songs/lenaRaineInfiniteAmethyst.mp3", "songs/alekseyChistilinOcean.mp3", "songs/stanislavBarsantovInterstellarTravelling.mp3", "songs/M83AnotherWaveFromYou.mp3"]
        self.songNames = ["Turn Away And Return - Hammock", "Aurora - Scott Buckley", "Cassini's Grand Finale - Erik Wernquist", "Wanderers - Cristian Sandquist", "Infinite Amethyst - Lena Raine", "Ocean - Aleksey Chistilin", "Interstellar Travelling - Stanislav Barsantov", "Another Wave From You - M83"]
        self.songLengths = [313, 498, 221, 230, 296, 212, 87, 113]

        self.gameEngine = gameEngine
        self.phase = 0
        self.playSong(0)
        self.tmp = 0

    def playSong(self, song):
        pygame.mixer.music.set_volume(0.1)
        self.startTime = time.time()
        self.length = self.songLengths[song]
        self.song = self.songNames[song]
        pygame.mixer.music.load(self.songs[song])
        pygame.mixer.music.play()

    def tick(self):
        if self.phase == 0 and self.gameEngine.playerDepth >= 200:
            pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - self.gameEngine.timers.deltaTime)

            if pygame.mixer.music.get_volume() <= 0:
                self.phase = 1
                self.playSong(1)

        if self.phase == 1 and self.gameEngine.playerDepth >= 1000:
            pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - (self.gameEngine.timers.deltaTime / 10))

            if pygame.mixer.music.get_volume() <= 0:
                self.phase = 2
                self.playSong(4)

        if self.phase == 2 and not pygame.mixer.music.get_busy():
            pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() -(self.gameEngine.timers.deltaTime / 10))

            if pygame.mixer.music.get_volume() <= 0:
                self.tmp += random.randint(1, 4)
                self.tmp = self.tmp % 5
                self.playSong(self.tmp)

        if self.phase == 2 and self.gameEngine.playerDepth >= (10914 - (abs(self.gameEngine.player.yVelocty * 87.67))) - 1000:
            self.phase = 3

        if self.phase == 3 and self.gameEngine.playerDepth >= 10914 - ((abs(self.gameEngine.player.yVelocity * 0.1) * 71.13)):
            pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - (self.gameEngine.timers.deltaTime / 10))

            if pygame.mixer.music.get_volume() <= 0:
                self.phase = 4
                self.playSong(6)

        if self.phase == 4 and self.gameEngine.ballastEnabled == 0:
            self.phase = 5
            self.playSong(5)

        if self.phase == 5 and self.gameEngine.playerDepth <= (abs(self.gameEngine.player.yVelocity * 0.1) * 113.8):
            pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - (self.gameEngine.timers.deltaTime / 10))

            if pygame.mixer.music.get_volume() <= 0:
                self.phase = 6
                self.playSong(7)

    def paint(self):
        pygame.draw.line(self.gameEngine.screen, (27, 27, 27), self.convertCoords(-229, 162.5, ""), self.convertCoords(-56, 162.5, ""), 2)
        pygame.draw.line(self.gameEngine.screen, (128, 128, 128), self.convertCoords(-229, 162.5, ""), self.convertCoords(-229 + (((time.time() - self.startTime) / self.length) * 173), 162.5, ""), 2)
