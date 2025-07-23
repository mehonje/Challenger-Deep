import pygame
import random

class SoundEffects:
    def __init__(self, gameEngine, costume = None):
        self.motorSound = pygame.mixer.Sound("sounds/subMotor1.mp3")
        self.underwaterAmbience = pygame.mixer.Sound("sounds/underwaterAmbience.mp3")
        self.whaleSounds = [pygame.mixer.Sound("sounds/whale1.mp3"), pygame.mixer.Sound("sounds/whale2.mp3"), pygame.mixer.Sound("sounds/whale3.mp3"), pygame.mixer.Sound("sounds/whale4.mp3")]
        self.bubbleSounds = [pygame.mixer.Sound("sounds/bubbles1.mp3"), pygame.mixer.Sound("sounds/bubbles2.mp3"), pygame.mixer.Sound("sounds/bubbles3.mp3"), pygame.mixer.Sound("sounds/bubbles4.mp3"), pygame.mixer.Sound("sounds/bubbles5.mp3"), ]
        self.waterSounds = [pygame.mixer.Sound("sounds/water1.mp3"), pygame.mixer.Sound("sounds/water2.mp3")]

        self.channels = {
        "motor": pygame.mixer.Channel(1),
        "ambience": pygame.mixer.Channel(2),
        "whales": pygame.mixer.Channel(3),
        "bubbles": pygame.mixer.Channel(4),
        "water": pygame.mixer.Channel(5),
        }

        setVolume(75, self.channels["ambience"])

        self.restartCountdowns = [0, 0, 0]

        self.gameEngine = gameEngine

    def tick(self):
        if not self.channels["motor"].get_busy():
            self.channels["motor"].play(self.motorSound)
        
        if not self.channels["ambience"].get_busy():
            self.channels["ambience"].play(self.underwaterAmbience)

        if not self.channels["whales"].get_busy():
            if self.restartCountdowns[0] <= 0:
                setVolume(10, self.channels["whales"])
                self.channels["whales"].play(random.choice(self.whaleSounds))
                self.restartCountdowns[0] = random.randint(10, 20)

        if not self.channels["bubbles"].get_busy():
            if self.restartCountdowns[1] <= 0:
                setVolume(random.randint(25, 50), self.channels["bubbles"])
                self.channels["bubbles"].play(random.choice(self.bubbleSounds))
                self.restartCountdowns[1] = random.randint(8, 16)

        if not self.channels["water"].get_busy():
            if self.restartCountdowns[2] <= 0:
                setVolume(random.randint(25, 50), self.channels["water"])
                self.channels["water"].play(random.choice(self.waterSounds))
                self.restartCountdowns[2] = random.randint(6, 12)

        setVolume(15 * abs(self.gameEngine.keys[pygame.K_w] - self.gameEngine.keys[pygame.K_s]), self.channels["motor"])

        for x in range(len(self.restartCountdowns)):
            self.restartCountdowns[x] -= self.gameEngine.timers.deltaTime

def setVolume(percent, channel):
    channel.set_volume(percent * 0.01)
