import pygame
from pygame.locals import *
from Game2 import Game2
from Setting import BackGround_Color, Map_height, Map_width, blit_text_mulline, caption_font, body_textfont
# from Menu import blit_text_mulline
# from Game1 import *

def intro_2():
    pygame.init()
    pygame.display.set_caption("Game1_intro")

    screen = pygame.display.set_mode((Map_width, Map_height))
    
    intro_caption = "    Game 2 \n\n" # 게임 설명의 제목 설정
    intro_lines = "      선인장에 닿으면 죽는다!\n\n\n\n" \
        "          시작하시겠습니까?\n\n                 (Y) / (N)" # 게임 설명의 본문 설정

    running = True

    while running:
        screen.fill((BackGround_Color)) 
        blit_text_mulline(screen, intro_caption, (400, 200), caption_font) # (400, 200) 좌표에 intro_caption을 caption_font로 표시
        blit_text_mulline(screen, intro_lines, (350, 300), body_textfont) # (350, 300) 좌표에 intro_lines를 body_textfont로 표시
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == KEYDOWN:
                if event.key == K_y: # y 키가 눌리면 게임을 시작
                    game = Game2()
                    game.run()
                    running = False # 게임을 시작하고 현재 화면을 종료

                if event.key == K_n: # n 키가 눌리면 게임 시작없이 화면을 종료
                    running = False

        

        pygame.display.update()
