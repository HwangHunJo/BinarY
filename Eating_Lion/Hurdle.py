import pygame
import random
from Setting import *

#장애물 클래스 생성
class hurdle:
    def __init__(self, parent_screen):
        spawn_x_start = 2 # 장애물의 x좌표를 (50 * 2)px 부터 생성
        self.images = [pygame.image.load(".//images//hurdle1.png"), pygame.image.load(".//images//hurdle2.png")] # 이미지 배열 속에 2개의 선인장 사진을 추가
        self.img_choice = random.randint(0, 1) # 이미지 2개중 하나를 선택하기위한 랜덤 변수
        self.image = self.images[self.img_choice] # 선택된 랜덤 변수를 이용해 이미지 가져오기
        self.image = pygame.transform.scale(self.image, (50, 50)) # 이미지의 크기를 50px * 50px로 설정 
        self.parent_screen = parent_screen # 생성될 화면을 설정
        self.x = random.randint(spawn_x_start, spawn_x_end) * 50 # 장애물의 x축 생성 위치 (100 ~ 1050)px
        self.y = random.randint(spawn_x_start, spawn_y_end) * 50 # 장애물의 y축 생성 위치 (50 ~ 550)px

    # 맵에 장애물 표시
    def draw(self):
        Map_objects[self.x // 50][self.y // 50] = True # 현재 장애물 위치를 True로 변경 (고기가 그 위치에 생성되지 않게 하기 위해서)
        self.parent_screen.blit(self.image, (self.x, self.y)) # 화면에 장애물 표시
