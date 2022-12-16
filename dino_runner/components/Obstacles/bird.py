import random
from dino_runner.components.Obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD
class Bird(Obstacle):

    def __init__(self, image):
        self.type = 1
        super().__init__(image, self.type)
        self.rect.y = 250


