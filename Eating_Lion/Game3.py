from decimal import Decimal
import pygame
from pygame.locals import *
import time
from Game_Pause import pausing
from Meat import *
from Lion import *
from Setting import *
from Thorn import *

class Game3:
    def __init__(self):
        pygame.init()
        self.secs = 0
        self.score = 0
        # 화면 세팅
        self.surface = pygame.display.set_mode((Map_width, Map_height))
        self.surface.fill(BackGround_Color)
        # 사자 생성, 표시
        self.Lion = Lion(self.surface)
        
        # 사자의 위치를 왼쪽 아래로 설정 (게임1, 2와 같이 왼쪽 위에서 생성될 시 생성된 후 즉시 가시에 닿아 죽을수 있음)
        self.Lion.x = 0 # x좌표는 가장 왼쪽인 0으로 설정
        self.Lion.y = Map_height - 100  # y좌표는 맵 크기에서 100을 뺀 가장 아래로 설정
        self.Lion.direction = "right" # 사자가 바라보는 방향을 오른쪽으로 설정해 시작하면 오른쪽으로 가게 설정
        self.Lion.draw()
        # 가시 생성
        self.Thorns = [] # 가시 배열 생성
        for i in range(ThornNum):
            self.Thorns.append(Thorn(self.surface)) # 가시 배열 안에 객체 생성
            self.Thorns[i].draw() # 배열 안에 있는 가시를 화면에 표시
        
        # 고기 생성
        self.meats = []
        for i in range(MeatNum):
            self.meats.append(Meat(self.surface, 7)) # 고기가 생성될 화면과 고기의 y생성 범위를 450px(7 * 50px)부터 시작으로 정함
            self.meats[i].draw()

    #게임이 진행되는 중 실행되는 함수
    def play(self):
        
        self.surface.blit(BackGround_Img3, (0, 0))
        
        self.score_line = body_textfont.render(f"Score : {self.score}", True, (0, 0, 0)) 
        self.now_time_line = body_textfont.render(f"{int(self.secs)}s", True, (0, 0, 0))
        self.surface.blit(self.now_time_line, (Map_width // 2 - 50, 10))
        self.surface.blit(self.score_line, (Map_width - 150, 10))
        
        self.Lion.walk() # 사자 이동

        for Thorn in self.Thorns:          
            Thorn.move() # 가시 움직이기
            Thorn.draw() # 가시 화면에 생성
            
            if Thorn.is_collision_Thorn(self.Lion.x, self.Lion.y): # 사자와 가시의 충돌 확인
                # 가시와 충돌했다면
                Eating_sound.stop() # 현재 먹는 소리 멈추고
                Thorn_sound.play() # 가시에 찔리는 소리를 재생
                raise "Game Over" # raise를 이용해 게임 종료
            if is_collision_Map(Thorn.x, Thorn.y): # 가시와 맵의 충돌 확인
                # 맵과 충돌했다면
                Thorn.reset_position() # 가시의 위치를 재조정 

            
        for meat in self.meats: # 고기 배열 속 고기를 꺼내와 화면에 표시
            meat.draw()
        
        
        # 사자와 화면의 충돌 확인
        if is_collision_Map(self.Lion.x, self.Lion.y):
            Eating_sound.stop()
            Death_sound.play()
            raise "Game Over"
        

        # 사자와 고기의 충돌 확인
        for meat in self.meats:
            if self.Lion.is_collision_With_Lion(meat.x, meat.y):
                Eating_sound.stop()
                Eating_sound.play()
                self.score += 1
                meat.move()

        pygame.display.flip()

    #게임이 끝났을때 화면에 표시하는 함수
    def show_game_over(self):
        global best_score
        self.surface.fill(BackGround_Color)
        self.surface.blit(GameOver_Img, (150, -70))
        
        if best_score < self.score: # 최고 점수가 현재 스코어와 비교 후 더 낮다면 교환
            best_score = self.score
    
        blit_text_mulline(self.surface, f"     {self.score} \n Score", (350, 200), caption_font)
        blit_text_mulline(self.surface, f"    {best_score} \n Best ", (600, 200), caption_font)
        blit_text_mulline(self.surface, "다시시작 - R \n 나가기 - E", (470, 400), body_textfont)
        pygame.display.flip()
    

    #게임 종료 후 R 키를 눌렀을때 재시작 하는 함수
    def reset(self):
        self.secs = 0
        self.score = 0

        # 사자를 생성, 위치 조정
        self.Lion = Lion(self.surface)
        self.Lion.x = 0
        self.Lion.y = Map_height - 100
        self.Lion.direction = "right"
        
        # 고기 재생성, 객체를 배열 속에 추가
        self.meats = []
        for i in range(MeatNum):
            self.meats.append(Meat(self.surface, 7))
            self.meats[i].draw()

        # 가시 재생성, 객체를 배열 속에 추가
        self.Thorns = []
        for _ in range(ThornNum):
            self.Thorns.append(Thorn(self.surface))

        # 모든 소리 멈추기
        Eating_sound.stop()
        Death_sound.stop()
        Thorn_sound.stop()

    #게임 시작
    def run(self):

        running = True
        pause = False #게임이 끝났을때 멈추도록 하는 변수

        while running:
            self.surface.blit(BackGround_Img3, (0, 0))
            

            self.secs += Decimal("0.15") # 게임이 0.15초마다 재시작되므로 0.15를 더해줌

            for event in pygame.event.get():
                
                #키가 눌렸다면
                if event.type == KEYDOWN:
                    
                    if event.key == K_ESCAPE: #눌려진 키가 Esc 키 라면 게임을 종료
                        pausing()
                        
                    if event.key == K_r: #눌려진 키가 R 키 라면 게임을 재시작
                        self.reset()
                        pause = False #게임이 다시 시작됨

                    if event.key == K_e:
                        running = False

                    #움직이는 과정
                    if not pause: #게임이 끝나지 않았다면
                        if event.key == K_UP: #위쪽 방향키가 눌렸을때 위로이동
                            self.Lion.move_up()
                        
                        if event.key == K_DOWN: #아래 방향키가 눌렸을때 아래로 이동
                            self.Lion.move_down()
                        
                        if event.key == K_LEFT: #왼쪽 방향키가 눌렸을때 왼쪽으로 이동
                            self.Lion.move_left()

                        if event.key == K_RIGHT: #오른쪽 방향키가 눌렸을때 오른쪽으로 이동
                            self.Lion.move_right()

                #게임 종료
                elif event.type == QUIT: #X 표시가 눌렸을 경우 게임을 종료
                    running = False

            #게임이 다시 시작되는 과정
            try:
                if not pause: #만약 pause가 False라면 게임을 계속해서 진행
                    self.play()

            except Exception as e: #그렇지 않다면 게임을 정지시키고 종료 화면을 보여줌
                self.show_game_over()
                pause = True

            time.sleep(0.15)
