from sprite import Sprite

class UI(Sprite):
    def __init__(self, gameEngine, costume = None):
        super().__init__(gameEngine, costume)

    def paint(self):
        if self.gameEngine.menu == 1:
            self.x, self.y = -140, 25
            self.setCostume("button.png")
            self.stamp(50, 100)
            
            if self.isClicked:
                self.gameEngine.menu = 2
                self.gameEngine.timers.timers[2] = 0

            self.setCostume("start button.png")
            self.stamp(0, 100)
        elif self.gameEngine.menu == 2:
            self.x, self.y = -120, 22.5
            self.setCostume("sub back.png")
            self.stamp(50, 100)

            if self.isClicked and self.gameEngine.timers.timers[2] > 30:
                self.gameEngine.ship = 1
                self.gameEngine.menu = 0

            self.setCostume("dsv limiting factor.png")
            self.stamp(0, 225)

            self.x, self.y = 120, 22.5
            self.setCostume("sub back.png")
            self.stamp(50, 100)

            if self.isClicked and self.gameEngine.timers.timers[2] > 30:
                self.gameEngine.ship = 2
                self.gameEngine.menu = 0

            self.setCostume("deepsea challenger.png")
            self.stamp(0, 170)