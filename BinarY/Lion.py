from random import choices
import pygame
#스네이크 클래스 생성
class Lion:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.body = pygame.image.load(".//images//lion1.png").convert_alpha()
        self.body = pygame.transform.scale(self.body, (50, 50))
        self.x = 50
        self.y = 50
        self.direction = "down"
        
    def change_img(self, choice):
        if choice == 1:
            self.body = pygame.image.load(".//images//lion1.png").convert_alpha()
        elif choice == 2:
            self.body = pygame.image.load(".//images//lion2.png").convert_alpha()
        
        self.body = pygame.transform.scale(self.body, (50, 50))

    #왼쪽 으로 움직이기
    def move_left(self):
        self.direction = "left"

    #오른쪽 으로 움직이기
    def move_right(self):
        self.direction = "right"
        
    #위로 움직이기
    def move_up(self):
        self.direction = "up"

    #아래로 움직이기
    def move_down(self):
        self.direction = "down"

    #맵에 스네이크 표시
    def draw(self):
        self.parent_screen.blit(self.body, (self.x, self.y))
    

    #매 초 움직이기
    def walk(self):
        if self.direction == "left":
            self.x -= 50
            self.change_img(2)
        if self.direction == "right":
            self.x += 50
            self.change_img(1)
        if self.direction == "up":
            self.y -= 50
        if self.direction == "down":
            self.y += 50
        
        self.draw()