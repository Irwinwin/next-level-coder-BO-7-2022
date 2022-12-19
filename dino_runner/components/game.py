import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS , CLOUD, DESERT
from dino_runner.components.Dinosaur import Dinosaur
from dino_runner.components.Obstacles.obstacle_manager import Obstacle_manager
from dino_runner.components.power_ups.power_ups_maganager import PowerUpManager

consolas = pygame.font.match_font('consolas')
negro = pygame.Color.b

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        pygame.mixer.init() #sonido
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        # Nubes
        self.x_pos_cloud = 100 
        self.y_pos_cloud = 100
        self.x_pos_cloud1 = 400 
        self.y_pos_cloud1 = 150
        #fondo
        self.x_pos_desert = 900 
        self.y_pos_desert = 400

        self.player = Dinosaur()
        self.Obstacle_manager = Obstacle_manager()
        self.points = 0
        self.power_up_manager = PowerUpManager()
        #musica
        pygame.mixer.music.load('dino_runner/sonido/fondoh.mp3')
        pygame.mixer.music.play(-1)

    def score(self):
        self.points += 1
        if self.points % 100 == 0:
            self.game_speed += 1

        print(self.score)

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   
                self.playing = False
  

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.Obstacle_manager.update(self.game_speed, self)
        self.power_up_manager.update(self.points, self.game_speed, self.player)
        self.score()
        self.player.check_invincibility()

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.Obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()


    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
        ##nube1
        image_cloud = CLOUD.get_width()
        self.screen.blit(CLOUD, (self.x_pos_cloud, self.y_pos_cloud))
        self.screen.blit(CLOUD, (image_cloud + self.x_pos_cloud, self.y_pos_cloud))
        if self.x_pos_cloud <= -image_cloud:
            self.screen.blit(CLOUD, (image_cloud + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
        #nube2
        image_cloud = CLOUD.get_width()
        self.screen.blit(CLOUD, (self.x_pos_cloud1, self.y_pos_cloud1))
        self.screen.blit(CLOUD, (image_cloud + self.x_pos_cloud1, self.y_pos_cloud1))
        if self.x_pos_cloud <= -image_cloud:
            self.screen.blit(CLOUD, (image_cloud + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
        #fondo esqueleto
        image_desert = DESERT.get_width()
        self.screen.blit(DESERT, (self.x_pos_desert, self.y_pos_desert))
        if self.x_pos_cloud <= -image_desert:
            self.screen.blit(DESERT, (image_desert + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
    