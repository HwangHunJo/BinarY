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
    
    intro_caption = "    Game 2 \n\n"
    intro_lines = "      선인장에 닿으면 죽는다!\n\n\n\n" \
        "         시작하시겠습니까?\n\n               (Y) / (N)"

    running = True

    while running:
        screen.fill((BackGround_Color)) 
        blit_text_mulline(screen, intro_caption, (400, 200), caption_font)
        blit_text_mulline(screen, intro_lines, (350, 300), body_textfont)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == KEYDOWN:
                if event.key == K_y:
                    game = Game2()
                    game.run()
                    running = False

                if event.key == K_n:
                    running = False

        

        pygame.display.update()

# intro_2()