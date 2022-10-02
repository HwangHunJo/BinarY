import pygame
import random
from Setting import *

#고기 클래스 생성
class Meat:
    def __init__(self, parent_screen, meat_spawn_y_start = 1):
        self.images = [pygame.image.load(".//images//meat1.png"), pygame.image.load(".//images//meat2.png"), pygame.image.load(".//images//meat3.png")]
        self.img_choice = random.randint(0, 2)
        self.image = self.images[self.img_choice]
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.parent_screen = parent_screen
        self.meat_spawn_y_start = meat_spawn_y_start
        self.x = random.randint(spawn_x_start, spawn_x_end) * 50
        self.y = random.randint(self.meat_spawn_y_start, spawn_y_end) * 50
        
    #맵에 고기 표시
    def draw(self):
        if Map_objects[self.x // 50][self.y // 50] == True:
            self.x = random.randint(spawn_x_start, spawn_x_end) * 50
            self.y = random.randint(self.meat_spawn_y_start, spawn_y_end) * 50

        self.parent_screen.blit(self.image, (self.x, self.y))

    #고기 랜덤 이동
    def move(self):
        Map_objects[self.x // 50][self.y // 50] = False
        self.x = random.randint(spawn_x_start, spawn_x_end) * 50
        self.y = random.randint(self.meat_spawn_y_start, spawn_y_end) * 50
        Map_objects[self.x // 50][self.y // 50] = True
        # self.draw()
        
