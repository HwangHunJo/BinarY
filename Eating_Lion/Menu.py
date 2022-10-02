import pygame
from Game1_intro import *
from Game2_intro import *
from Game3_intro import *

# 게임 이동을 위한 버튼 클래스 생성
class Button:
    def __init__(self, x, y, image, scale): # x좌표, y좌표, 이미지, 이미지의 크기(2배, 3배, 4배 ...)
        width = image.get_width() # 이미지의 가로 크기 불러오기
        height = image.get_height() # 이미지의 세로 크기 불러오기
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale))) # 이미지의 크기를 (가로 * 크기) * (세로 * 크기)로 설정 
        self.rect = self.image.get_rect() # 이미지의 크기 
        self.rect.topleft = (x, y) # 버튼이 클릭되었을때 확인을 위해 왼쪽 위 좌표를 x, y로 설정
        self.clicked = False # 마우스가 클릭 됐는지 판단하는 boolean 변수

    # 화면에 버튼 생성, 클릭 되었는지 확인
    def draw(self, surface):
        action = False # 사용자의 행동을 감지하는 변수(기본 설정은 False)
        pos = pygame.mouse.get_pos() # 마우스의 위치 불러오기

        if self.rect.collidepoint(pos): # 버튼의 이미지가 마우스의 위치와 닿았는지 확인
            # 닿았다면
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False: # 마우스의 왼쪽버튼(pygame.mouse.get_pressed()[0])과 마우스가 클릭 됐다가 떼어졌는지(self.clicked == False) 확인
                # 클릭 됐다면
                self.clicked = True # 마우스를 클릭한 상태로 변경
                action = True # 행동이 감지 된 상태로 변경

        if pygame.mouse.get_pressed()[0] == 0: # 마우스의 왼쪽버튼(pygame.mouse.get_pressed()[0])이 눌려졌는지 확인
            # 눌려지지 않았다면
            self.clicked = False # 마우스를 클릭하지 않은 상태로 변경 
            
        surface.blit(self.image, (self.rect.x, self.rect.y)) # 화면에 표시
        
        return action # 사용자의 행동을 return

pygame.init()

screen = pygame.display.set_mode((Map_width, Map_height)) # 화면 크기 설정
pygame.display.set_caption("Lion Running") # 제목 설정

font1 = pygame.font.SysFont("arialblack", 80) # 첫번째 폰트 불러오기
font2 = pygame.font.Font("fonts\MaplestoryFont_TTF\Maplestory Light.ttf", 30) # 두번째 폰트 불러오기

Text_Col = (255, 255, 255) # 문자(텍스트)의 색깔을 하얀색으로 설정

game1_img = pygame.image.load(".//images//Buttons//Game1.png").convert_alpha() # 게임 1 버튼 이미지 불러오기
game2_img = pygame.image.load(".//images//Buttons//Game2.png").convert_alpha() # 게임 2 버튼 이미지 불러오기
game3_img = pygame.image.load(".//images//Buttons//Game3.png").convert_alpha() # 게임 3 버튼 이미지 불러오기
quit_img = pygame.image.load(".//images//Buttons//Quit.png").convert_alpha() # 게임 종료 버튼 이미지 불러오기

game1_button = Button(200, 150, game1_img, 1) # 게임 1 버튼 생성(200px, 120px에 game1_img를 이미지로 하고 크기는 1배) 
game2_button = Button(200, 275, game2_img, 1) # 게임 2 버튼 생성(200px, 245px에 game2_img를 이미지로 하고 크기는 1배)
game3_button = Button(200, 400, game3_img, 1) # 게임 3 버튼 생성(200px, 370px에 game3_img를 이미지로 하고 크기는 1배)
quit_button = Button(200, 525, quit_img, 1) # 종료 버튼 생성(200px, 495px에 quit_img를 이미지로 하고 크기는 1배)

# 게임 방법 소개 글
Main_intro_line = "게임 방법 \n\n"\
        "이동 : 화살표(↑ ↓ ← →) \n\n"\
        "일시 정지/해제 : ESC \n\n"\
        "재시작 : R \n\n"\
        "게임 종료 : E\n\n"

running = True

while running:
    screen.fill((122, 199, 82)) # 화면을 rgb(122, 199, 82)색깔로 채움
    pygame.draw.rect(screen, (255, 255, 255), (500, 150, 400, 450)) # screen의 (500, 150) 좌표에 가로가 400이고 세로가 450인 하얀색 사각형을 생성 
    blit_text_mulline(screen, "Eating_Lion", (300, 20), font1, Text_Col) # screen의 (300, 20) 좌표에 "Eating_Lion"문자열을 font1로 하고 하얀색으로 표시
    blit_text_mulline(screen, Main_intro_line, (520, 200), font2) # screen의 (520, 200) 좌표에 Main_intro_line 문자열을 font2로 하고 검은색으로 표시 
    
    # 버튼이 클릭되었을때
    if game1_button.draw(screen): # 게임 1 버튼이 클릭되었을때
        intro_1()
    
    if game2_button.draw(screen): # 게임 2 버튼이 클릭되었을때
        intro_2()
    
    if game3_button.draw(screen): # 게임 3 버튼이 클릭되었을때
        intro_3()
            
    if quit_button.draw(screen): # 게임 종료 버튼이 클릭되었을때
        running = False
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_e: # e 키가 눌리면 게임 종료
                running = False
        if event.type == pygame.QUIT: # X 표시가 눌리면 게임 종료
            running = False

    pygame.display.update()

pygame.quit()