import random
import pygame
from Setting import *

#가시 클래스 생성
class Thorn:
    def __init__(self, parent_screen):
        self.Thorn_img = pygame.image.load(".//images//thorn.png") # 가시 이미지 설정
        self.Thorn_img = pygame.transform.scale(self.Thorn_img, (50, 50)) # 가시 이미지의 크기를 50px * 50px 로 설정

        self.parent_screen = parent_screen # 가시가 생성될 화면 설정

        self.y = 10 # 가시의 y축 생성 위치
        self.x = random.randint(1, spawn_x_end) * 50 # 가시의 x축 생성 위치 (50 ~ 1050)px
        self.speed = random.randint(3, 5) * 10  # 가시의 떨어지는 속도 설정 (30 ~ 50)px

    # 가시 생성
    def draw(self):
        self.parent_screen.blit(self.Thorn_img, (self.x, self.y)) # 화면에 가시 생성

    # 가시의 움직임
    def move(self): 
        self.y += self.speed # 가시가 현재 설정된 speed 만큼 이동
        self.draw() # 그 후 화면에 생성

    # 가시가 맵의 끝에 갔을때 x, y, speed 를 재설정 
    def reset_position(self):
        self.x = random.randint(1, spawn_x_end) * 50 # 가시의 x축 생성 위치 (50 ~ 1050)px
        self.speed = random.randint(3, 5) * 10 # 가시의 떨어지는 속도 설정 (30 ~ 50)px
        self.y = 10 # 가시의 y축 생성 위치
    
    # 어떤 물체가 가시와 닿았을때 상호작용 (사자와 가시)
    def is_collision_Thorn(self, x1, y1):
        if self.x >= x1 and self.x <= x1 + 50: # 가시의 x좌표가 다른 물체의 왼쪽 x좌표(x1) 이상이고 오른쪽 x좌표(x1 + 50) 이하이면서
            if self.y >= y1 and self.y <= y1 + 50: # 가시의 y좌표가 다른 물체의 위쪽 y좌표(y1) 이상이고 아래쪽 y좌표(y1 + 50) 이하 라면
                return True # True를 반환
        
        
        return False # 그게 아니면 False를 반환

