from sprite import Sprite
import pygame
from math import floor

class TextEngine(Sprite):
    def __init__(self, gameEngine, costume = None):
        super().__init__(gameEngine, costume)
        self.fontSetups = {}

    def text(self, text, position, align, colour, font, size):
        fontSetup = (font, size * (self.gameEngine.width / 480))
        if fontSetup not in self.fontSetups:
            self.fontSetups[fontSetup] = pygame.font.SysFont(font, int(size * (self.gameEngine.width / 480)))
        font = self.fontSetups[fontSetup]

        x, y = self.convertCoords(position[0], position[1])
        textRect = font.render(text, True, colour).get_rect()
        if align == "c":
            x -= font.size(text)[0] / 2
        elif align == "r":
            x -= font.size(text)[0]
        y -= font.size(text)[1] / 2
        
        self.screen.blit(font.render(text, True, colour), (x, y))
        
    def paint(self):
        if self.gameEngine.menu == 0:
            self.text(f"{floor(self.gameEngine.playerDepth)}m", (0, 165), "c", (255, 255, 255), "Sans Serif", 28)

            self.text(f"SPEED   {abs(floor(self.gameEngine.player.yVelocity * 100) / 1000)} m/s", (-230, -130), "l", (255, 255, 255), "Sans Serif", 14)

            self.text(f"DEPTH   {abs(floor(self.gameEngine.playerDepth * 1000) / 1000)} m", (-230, -140), "l", (255, 255, 255), "Sans Serif", 14)

            #temperature
            tmp = 25
            if self.gameEngine.playerDepth > 0 and self.gameEngine.playerDepth < 1000:
                tmp = 25 - (0.02 * (self.gameEngine.playerDepth))
            elif self.gameEngine.playerDepth > 1000 and self.gameEngine.playerDepth < 4000:
                tmp = 5 - (0.0004 * (self.gameEngine.playerDepth - 1000))
            elif self.gameEngine.playerDepth > 4000:
                tmp = 1.4
            self.text(f"TEMP.   {floor(tmp * 1000) / 1000} °C", (-230, -150), "l", (255, 255, 255), "Sans Serif", 14)

            #light
            tmp = "off"
            match self.gameEngine.light.lightSetting:
                case 1:
                    tmp = "medium"
                case 2:
                    tmp = "high"
            self.text(f"LIGHT   {tmp}", (-230, -160), "l", (255, 255, 255), "Sans Serif", 14)

            self.text(f"PRES.   {floor((1 + (self.gameEngine.playerDepth / 10)) * 1000) / 1000} atm", (-230, -170), "l", (255, 255, 255), "Sans Serif", 14)

            self.text(self.gameEngine.music.song, (-230, 170), "l", (255, 255, 255), "Sans Serif", 14)

            #Sunlight Zone data
            if self.gameEngine.playerDepth > -3 and self.gameEngine.playerDepth < 42.5:
                self.text("The Sunlight Zone", (60, -150 - self.gameEngine.camY), "l", (255, 255, 255), "Sans Serif", 21)
                self.text("(0m-200m)", (60, -165 - self.gameEngine.camY), "l", (255, 255, 255), "Sans Serif", 18)
                self.text("90% of all marine life lives", (60, -180 - self.gameEngine.camY), "l", (255, 255, 255), "Sans Serif", 14)
                self.text(" in the Sunlight Zone", (60, -190 - self.gameEngine.camY), "l", (255, 255, 255), "Sans Serif", 14)
                self.text("This is the only layer where", (60, -200 - self.gameEngine.camY), "l", (255, 255, 255), "Sans Serif", 14)
                self.text(" photosynthesis, a plant's", (60, -210 - self.gameEngine.camY), "l", (255, 255, 255), "Sans Serif", 14)
                self.text(" ability to produce nutrients", (60, -220 - self.gameEngine.camY), "l", (255, 255, 255), "Sans Serif", 14)
                self.text(" using sunlight, can occur", (60, -230 - self.gameEngine.camY), "l", (255, 255, 255), "Sans Serif", 14)

            #Twilight Zone data
            if self.gameEngine.playerDepth > 182 and self.gameEngine.playerDepth < 226.5:
                self.text("The Twilight Zone", (60, -2000 - self.gameEngine.camY), "l", (255, 255, 255), "Sans Serif", 21)
                self.text("(200m-1000m)", (60, -2015 - self.gameEngine.camY), "l", (255, 255, 255), "Sans Serif", 18)
                self.text("The pressure at 1000m is", (60, -2030 - self.gameEngine.camY), "l", (255, 255, 255), "Sans Serif", 14)
                self.text(" the same as ten elephants", (60, -2040 - self.gameEngine.camY), "l", (255, 255, 255), "Sans Serif", 14)
                self.text(" standing on your head", (60, -2050 - self.gameEngine.camY), "l", (255, 255, 255), "Sans Serif", 14)
                self.text("Almost none of the Twilight", (60, -2060 - self.gameEngine.camY), "l", (255, 255, 255), "Sans Serif", 14)
                self.text(" Zone and beyond has been", (60, -2070 - self.gameEngine.camY), "l", (255, 255, 255), "Sans Serif", 14)
                self.text(" explored", (60, -2080 - self.gameEngine.camY), "l", (255, 255, 255), "Sans Serif", 14)

            #Midnight Zone data
            if self.gameEngine.playerDepth > 982 and self.gameEngine.playerDepth < 1026:
                self.text("The Midnight Zone", (60, -10000 - self.gameEngine.camY), "l", (255, 255, 255), "Sans Serif", 21)
                self.text("(1000m-4000m)", (60, -10015 - self.gameEngine.camY), "l", (255, 255, 255), "Sans Serif", 18)
                self.text("The Midnight Zone is the", (60, -10030 - self.gameEngine.camY), "l", (255, 255, 255), "Sans Serif", 14)
                self.text(" largest habitat onsc Earth,", (60, -10040 - self.gameEngine.camY), "l", (255, 255, 255), "Sans Serif", 14)
                self.text(" containing 70% of all", (60, -10050 - self.gameEngine.camY), "l", (255, 255, 255), "Sans Serif", 14)
                self.text(" seawater", (60, -10060 - self.gameEngine.camY), "l", (255, 255, 255), "Sans Serif", 14)
                self.text("No sunlight reaches the", (60, -10070 - self.gameEngine.camY), "l", (255, 255, 255), "Sans Serif", 14)
                self.text(" Midnight Zone", (60, -10080 - self.gameEngine.camY), "l", (255, 255, 255), "Sans Serif", 14)

            #Abyssal Zone data
            if self.gameEngine.playerDepth > 3982 and self.gameEngine.playerDepth < 4027.5:
                self.text("The Abyssal Zone", (60, -40000 - self.gameEngine.camY), "l", (255, 255, 255), "Sans Serif", 21)
                self.text("(4000m-6000m)", (60, -40015 - self.gameEngine.camY), "l", (255, 255, 255), "Sans Serif", 18)
                self.text("The pressure in the Abyssal", (60, -40030 - self.gameEngine.camY), "l", (255, 255, 255), "Sans Serif", 14)
                self.text(" Zone reaches 600", (60, -40040 - self.gameEngine.camY), "l", (255, 255, 255), "Sans Serif", 14)
                self.text(" atmospheres", (60, -40050 - self.gameEngine.camY), "l", (255, 255, 255), "Sans Serif", 14)
                self.text("The water in the Abyssal", (60, -40060 - self.gameEngine.camY), "l", (255, 255, 255), "Sans Serif", 14)
                self.text(" Zone has almost no oxygen", (60, -40070 - self.gameEngine.camY), "l", (255, 255, 255), "Sans Serif", 14)
                self.text(" in it", (60, -40080 - self.gameEngine.camY), "l", (255, 255, 255), "Sans Serif", 14)
        elif self.gameEngine.menu == 1:
            self.text("Challenger Deep", (0, 112.5), "c", (255, 255, 255), "Sans Serif", 42)
            self.text(self.gameEngine.music.song, (-230, 170), "l", (255, 255, 255), "Sans Serif", 14)
        elif self.gameEngine.menu == 2:
            self.text("Ship Selection", (0, 135), "c", (255, 255, 255), "Sans Serif", 28)
            self.text("DSV Limiting Factor", (-120, 105), "c", (255, 255, 255), "Sans Serif", 17.57308)
            self.text("Top Speed: 1.135m/s", (-195, -60), "l", (255, 255, 255), "Sans Serif", 14)
            self.text("Certified Depth: 11,000m", (-195, -75), "l", (255, 255, 255), "Sans Serif", 14)
            self.text("Crush Depth: 14,000m", (-195, -90), "l", (255, 255, 255), "Sans Serif", 14)
            self.text("Builder: Triton Submarines", (-195, -105), "l", (255, 255, 255), "Sans Serif", 14)

            self.text("Deepsea Challenger", (120, 105), "c", (255, 255, 255), "Sans Serif", 17.57308)
            self.text("Top Speed: 1.725m/s", (45, -60), "l", (255, 255, 255), "Sans Serif", 14)
            self.text("Certified Depth: 11,000m", (45, -75), "l", (255, 255, 255), "Sans Serif", 14)
            self.text("Crush Depth: 11,750m", (45, -90), "l", (255, 255, 255), "Sans Serif", 14)
            self.text("Builder: Acheron Project", (45, -105), "l", (255, 255, 255), "Sans Serif", 14)
