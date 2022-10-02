import pygame
from Setting import BackGround_Color, Map_height, Map_width, blit_text_mulline, caption_font, body_textfont

def pausing():
    pygame.init()
    pygame.display.set_caption("Paused")

    screen = pygame.display.set_mode((Map_width, Map_height))
    running = True

    while running:
        screen.fill((BackGround_Color))
        blit_text_mulline(screen, "일시 정지", (400, 200), caption_font)
        blit_text_mulline(screen, "..ESC키를 눌러 계속..", (400, 300), body_textfont)

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    running = False
                    
        
        pygame.display.update()

