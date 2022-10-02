from decimal import Decimal
import pygame
from pygame.locals import *
import time
from Meat import *
from Lion import *
from Setting import *
from Game_Pause import pausing


def Reset():
    global best_score
    global best_time
    
    best_score = 0
    best_time = 0



#게임 실행
class Game1:
    def __init__(self):
        pygame.init()
        self.secs = secs
        self.score = score
        #화면 세팅
        self.surface = pygame.display.set_mode((Map_width, Map_height))
        self.surface.fill(BackGround_Color)
        # self.surface.blit(BackGround_Img, (0, 0))
        #스네이크 생성, 표시
        self.Lion = Lion(self.surface)
        self.Lion.draw()
        #고기 생성, 표시
        self.meats = []
        for i in range(MeatNum):
            self.meats.append(Meat(self.surface))
            self.meats[i].draw()
        self.char_speed = 0.3


    #게임이 끝났을때 화면에 표시하는 함수
    def show_game_over(self):
        global best_score
        global best_time
        self.surface.fill(BackGround_Color)
        
        if best_score < self.score:
            best_score = self.score
        if best_time < self.secs:
            best_time = self.secs
       
        # best_score_line = body_textfont.render(f"{best_score} \n Best", True, (0, 0, 0))
        # self.surface.blit(best_score_line, (200, 100))
        # best_time_line = self.font.render(f"Your Best Time : {int(best_time)}s", True, (0, 0, 0))
        # self.surface.blit(best_time_line, (200, 150))
        blit_text_mulline(self.surface, f"     {self.score} \n Score", (300, 200), caption_font)
        blit_text_mulline(self.surface, f"    {best_score} \n Best ", (500, 200), caption_font)
        blit_text_mulline(self.surface, "다시시작 - R \n 나가기 - E", (400, 400), body_textfont)
        # line1 = body_textfont.render(f"{self.score} \n Score", True, (0, 0, 0))
        # self.surface.blit(line1, (200, 300))
        # line2 = self.font.render(f"To play again press R. If not, Press Esc ", True, (0, 0, 0))
        # self.surface.blit(line2, (200, 350))
        pygame.display.flip()

    #게임이 진행되는 중 실행되는 함수
    def play(self):
        
        # self.surface.fill((BackGround_Color))
        
        self.surface.blit(BackGround_Img1, (0, 0))
        self.score_line = body_textfont.render(f"Score : {self.score}", True, (0, 0, 0))
        self.now_time_line = body_textfont.render(f"{int(self.secs)}s", True, (0, 0, 0))
        self.Lion.walk()
        
        for meat in self.meats:
            meat.draw()
        
        self.surface.blit(self.now_time_line, (Map_width // 2 - 50, 10))
        self.surface.blit(self.score_line, (Map_width - 150, 10))
        
        pygame.display.flip()

        #Lion 와 Meat의 충돌 확인
        
        for meat in self.meats:
            if is_collision_With_Lion(self.Lion.x, self.Lion.y, meat.x, meat.y):
                Eating_sound.stop()
                self.score += 1
                Eating_sound.play()
                if self.char_speed > 0.1:
                    self.char_speed = Decimal(str(self.char_speed)) - Decimal("0.007")
                meat.move()


        #Sanke 와 화면의 충돌 확인
        if is_collision_Map(self.Lion.x, self.Lion.y):
            Eating_sound.stop()
            Death_sound.play()
            raise "Game Over"

    #게임 종료 후 R 키를 눌렀을때 재시작 하는 함수
    def reset(self):
        self.score = 0
        self.secs = 0
        self.char_speed = 0.3
        self.Lion = Lion(self.surface)
        self.meats = []
        Eating_sound.stop()
        Death_sound.stop()
        for _ in range(MeatNum):
            self.meats.append(Meat(self.surface))


    #게임 시작
    def run(self):
        running = True
        pause = False #게임이 끝났을때 멈추도록 하는 변수
        
        while running:
            
            self.surface.blit(BackGround_Img1, (0, 0))
            
            #초를 세는 과정
            
            self.secs += Decimal(str(self.char_speed)) / Decimal("1.0") 
            

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

            time.sleep(float(self.char_speed))

# game = Game1()
# game.run()