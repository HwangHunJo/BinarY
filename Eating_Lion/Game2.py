from decimal import Decimal
import pygame
from pygame.locals import *
import time
from Game_Pause import pausing
from Meat import *
from Lion import *
from Setting import *
from Hurdle import *

#게임 실행
class Game2:
    def __init__(self):
        pygame.init()
        self.score = 0
        self.secs = 0
        #화면 세팅
        self.surface = pygame.display.set_mode((Map_width, Map_height))
        self.surface.fill((BackGround_Color))
        #스네이크 생성, 표시
        self.Lion = Lion(self.surface)
        self.Lion.draw()
        #고기 생성, 표시
        self.meats = []
        for i in range(MeatNum):
            self.meats.append(Meat(self.surface))
            self.meats[i].draw()
        
        #장애물 생성, 표시
        self.hurdles = [] # 장애물 배열 생성
        for i in range(HurdleNum): 
            self.hurdles.append(hurdle(self.surface)) # 장애물 배열 안에 객체 생성
            self.hurdles[i].draw() # 배열 안에 있는 장애물을 화면에 표시

    #게임이 진행되는 중 실행되는 함수
    def play(self):

        self.surface.blit(BackGround_Img2, (0, 0))
        
        self.score_line = body_textfont.render(f"Score : {self.score}", True, (0, 0, 0)) 
        self.now_time_line = body_textfont.render(f"{int(self.secs)}s", True, (0, 0, 0))
        self.surface.blit(self.now_time_line, (Map_width // 2 - 50, 10))
        self.surface.blit(self.score_line, (Map_width - 150, 10))
        
        self.Lion.walk()

        for meat in self.meats:
            meat.draw()

        for hurdle in self.hurdles: # 장애물 배열 속 장애물을 꺼내와 화면에 표시
            hurdle.draw()

        
        for meat in self.meats:
            if self.Lion.is_collision_With_Lion(meat.x, meat.y): # 사자와 고기의 충돌 확인
                Eating_sound.stop()
                Eating_sound.play()
                self.score += 1
                meat.move()

        
        if is_collision_Map(self.Lion.x, self.Lion.y): # 사자와 화면의 충돌 확인
            Eating_sound.stop()
            Death_sound.play()
            raise "Game Over"

        
        for hurdle in self.hurdles:
            if self.Lion.is_collision_With_Lion(hurdle.x, hurdle.y): #Lion 와 hurdle의 충돌 확인
                # 충돌 했다면
                Eating_sound.stop() # 현재 재생중인 먹는 소리를 멈추고 
                Death_sound.play() # 죽는 소리를 재생시킨다
                raise "Game Over" # raise를 이용해 게임 종료

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
    
    
    def reset(self): #게임 종료 후 R 키를 눌렀을때 재시작 하는 함수
        self.score = 0
        self.secs = 0
        self.Lion = Lion(self.surface)
        
        # 고기 재생성, 객체를 배열 속에 추가
        self.meats = []
        for _ in range(MeatNum):
            self.meats.append(Meat(self.surface))
        
        # 장애물 재생성, 객체를 배열 속에 추가
        self.hurdles = []
        for _ in range(HurdleNum):
            self.hurdles.append(hurdle(self.surface))

        # 모든 소리 멈추기
        Eating_sound.stop()
        Death_sound.stop()
        

    #게임 시작
    def run(self):
        
        running = True
        pause = False #게임이 끝났을때 멈추도록 하는 변수

        while running:
            
            self.surface.blit(BackGround_Img2, (0, 0))

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
