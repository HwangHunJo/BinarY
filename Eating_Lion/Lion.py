import pygame
# 사자 클래스 생성
class Lion:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen # 생성될 화면 설정
        self.body = pygame.image.load(".//images//lion1.png").convert_alpha() # 사자 이미지 불러오기
        self.body = pygame.transform.scale(self.body, (50, 50)) # 사자의 크기를 50px * 50px로 설정
        
        # 처음 생성 위치, 바라보고 있을 방향 설정 
        self.x = 50 
        self.y = 50
        self.direction = "down"
    
    # 사자 이미지 변경을 위한 함수
    def change_img(self, choice):
        if choice == 1: # choice == 1 즉, 오른쪽 방향키가 눌렸을때
            self.body = pygame.image.load(".//images//lion1.png").convert_alpha() # 사자가 오른쪽을 바라보고 있는 이미지로 변경
        elif choice == 2: # choice == 2 즉, 왼쪽 방향키가 눌렸을때
            self.body = pygame.image.load(".//images//lion2.png").convert_alpha() # 사자가 왼쪽을 바라보고 있는 이미지로 변경
        
        self.body = pygame.transform.scale(self.body, (50, 50)) # 사자의 크기를 50px * 50px로 설정

    # 왼쪽 으로 움직이기
    def move_left(self):
        self.direction = "left"

    # 오른쪽 으로 움직이기
    def move_right(self):
        self.direction = "right"
        
    # 위로 움직이기
    def move_up(self):
        self.direction = "up"

    # 아래로 움직이기
    def move_down(self):
        self.direction = "down"

    # 맵에 사자 표시
    def draw(self):
        self.parent_screen.blit(self.body, (self.x, self.y))

    def is_collision_With_Lion(self, x2, y2): # 사자와 충돌을 확인하는 함수
        if self.x == x2: # 사자의 x가 x2의 좌표와 완전히 같다면
            if self.y == y2: # 사자의 y가 y2의 좌표와 완전히 같다면
                return True # True를 return
        
        # 아니라면
        return False # False를 return 

    # 매 초 움직이기
    def walk(self):

        if self.direction == "left": # 왼쪽 방향키가 눌리면
            self.x -= 50 # 왼쪽으로 50px 만큼 이동
            self.change_img(2) # 매개변수 choice를 2로 하는 함수 실행

        if self.direction == "right": # 오른쪽 방향키가 눌리면
            self.x += 50 # 오른쪽으로 50px 만큼 이동
            self.change_img(1) # 매개변수 choice를 2로 하는 함수 실행

        if self.direction == "up": # 위쪽 방향키가 눌리면
            self.y -= 50 # 위쪽으로 50px 만큼 이동

        if self.direction == "down": # 아래 방향키가 눌리면
            self.y += 50 # 아래쪽으로 50px 만큼 이동
        
        self.draw() # 화면에 표시