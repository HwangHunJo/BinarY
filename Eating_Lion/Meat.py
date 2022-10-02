import pygame
import random
from Setting import *

# 고기 클래스 생성
class Meat:
    def __init__(self, parent_screen, meat_spawn_y_start = 1):
        self.images = [pygame.image.load(".//images//meat1.png"), pygame.image.load(".//images//meat2.png"), pygame.image.load(".//images//meat3.png")] # 이미지 배열 속에 3개의 고기 사진을 추가
        self.img_choice = random.randint(0, 2) # 이미지를 선택할 랜덤 변수 생성
        self.image = self.images[self.img_choice] # 선택된 랜덤 변수로 이미지 불러오기
        self.image = pygame.transform.scale(self.image, (50, 50)) # 이미지를 50px * 50px로 설정
        self.parent_screen = parent_screen # 생성될 화면 설정
        self.meat_spawn_y_start = meat_spawn_y_start # 매개변수에 저장되어있는 고기가 생성될 y좌표의 시작을 불러오기
        self.x = random.randint(spawn_x_start, spawn_x_end) * 50 # 고기의 x축 생성 위치 (50 ~ 1050)px
        self.y = random.randint(self.meat_spawn_y_start, spawn_y_end) * 50 # 고기의 y축 생성 위치 (meat_spawn_y_start * 50 ~ 550)px
        
    # 맵에 고기 표시
    def draw(self):
        if Map_objects[self.x // 50][self.y // 50] == True: # 고기의 위치가 장애물, 다른 고기의 위치와 겹치는지 확인
            # 겹친다면
            self.x = random.randint(spawn_x_start, spawn_x_end) * 50 # x좌표 재설정
            self.y = random.randint(self.meat_spawn_y_start, spawn_y_end) * 50 # y좌표 재설정

        self.parent_screen.blit(self.image, (self.x, self.y)) # 화면에 고기 생성

    # 고기 랜덤 이동
    def move(self):
        Map_objects[self.x // 50][self.y // 50] = False # 현재 위치를 False로 바꾸고
        self.x = random.randint(spawn_x_start, spawn_x_end) * 50 # x좌표 재설정
        self.y = random.randint(self.meat_spawn_y_start, spawn_y_end) * 50 # y좌표 재설정
        Map_objects[self.x // 50][self.y // 50] = True # 바뀐 위치를 True로 설정
        self.draw() # 맵에 고기 표시
        
