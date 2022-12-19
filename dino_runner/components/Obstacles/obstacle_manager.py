import pygame
import random
from dino_runner.components.Obstacles.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS ,BIRD
from dino_runner.components.Obstacles.bird import Bird
from dino_runner.components.Dinosaur import Dinosaur

class Obstacle_manager:

    def __init__(self):
        self.obstacles = []
        self.hp = 1

    def update(self, game_speed, game):
        if len(self.obstacles) == 0:
            type = random.randint(0, 2)
            match type:
                case 0:
                    self.obstacles.append(Cactus(SMALL_CACTUS))
                case 1:
                    self.obstacles.append(Bird(BIRD))
                case 2:
                    self.obstacles.append(Cactus(LARGE_CACTUS))

        for obstacle in self.obstacles:
            obstacle.update(game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.shield:
                    Dinosaur.hp -= 1
                    pygame.time.delay(300)
                    #game.playing = False
                    obstacle.hp -=1
                    if obstacle.hp <= 0:
                        self.obstacles.pop()
                    break
                else:
                    self.obstacles.pop()

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
