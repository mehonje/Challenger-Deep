import time
from sprite import Sprite

class Timers(Sprite):
    def __init__(self, gameEngine, costume):
        super().__init__(gameEngine, costume)
        self.fps = 0
        self.deltaTime = 0
        self.lastTime = time.time()
        self.timers = [0, 0]

    def tick(self):
        self.fps = 1 / (time.time() - self.lastTime)
        self.deltaTime = time.time() - self.lastTime
        self.lastTime = time.time()
        for x in range(0, len(self.timers)):
            self.timers[x] = self.timers[x] + 1
