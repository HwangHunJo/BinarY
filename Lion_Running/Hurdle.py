import pygame
import random
from Setting import *

#장애물 클래스 생성
class hurdle:
    def __init__(self, parent_screen):
        spawn_x_start = 2
        self.images = [pygame.image.load(".//images//hurdle1.png"), pygame.image.load(".//images//hurdle2.png")]
        self.img_choice = random.randint(0, 1)
        self.image = self.images[self.img_choice]
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.parent_screen = parent_screen
        self.x = random.randint(spawn_x_start, spawn_x_end) * 50
        self.y = random.randint(spawn_x_start, spawn_y_end) * 50

    #맵에 장애물 표시
    def draw(self):
        Map_objects[self.x // 50][self.y // 50] = True
        self.parent_screen.blit(self.image, (self.x, self.y))
