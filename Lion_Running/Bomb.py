import random
import pygame
from Setting import *

class Bomb:
    def __init__(self, parent_screen):
        self.bomb_img = pygame.image.load(".//images//bomb.png")
        self.bomb_img = pygame.transform.scale(self.bomb_img, (50, 50))
        self.parent_screen = parent_screen
        self.y = 10
        self.x = random.randint(1, spawn_x_end) * 50
        self.speed = random.randint(3, 5) * 10  

    def draw(self):
        self.parent_screen.blit(self.bomb_img, (self.x, self.y))

    def move(self):
        self.y += self.speed
        self.draw()

    def reset_position(self):
        self.x = random.randint(1, spawn_x_end) * 50
        self.speed = random.randint(3, 5) * 10
        self.y = 10
    
    def is_collision_bomb(self, x1, y1):
        if self.x >= x1 and self.x <= x1 + 50:
            if self.y >= y1 and self.y <= y1 + 50:
                return True
        
        
        return False

