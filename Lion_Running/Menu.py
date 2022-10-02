import pygame
from Game1_intro import *
from Game2_intro import *
from Game3_intro import *

class Button:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False 
            
        surface.blit(self.image, (self.rect.x, self.rect.y))
        
        return action

pygame.init()

screen = pygame.display.set_mode((Map_width, Map_height))
pygame.display.set_caption("Lion Running")

font1 = pygame.font.SysFont("arialblack", 80)
font2 = pygame.font.Font("fonts\MaplestoryFont_TTF\Maplestory Light.ttf", 30)
# print(pygame.font.get_fonts())

Text_Col = (255, 255, 255)

game1_img = pygame.image.load(".//images//Buttons//Game1.png").convert_alpha()
game2_img = pygame.image.load(".//images//Buttons//Game2.png").convert_alpha()
game3_img = pygame.image.load(".//images//Buttons//Game3.png").convert_alpha()
quit_img = pygame.image.load(".//images//Buttons//Quit.png").convert_alpha()


# intro_img = pygame.image.load("") 

game1_button = Button(200, 120, game1_img, 1)
game2_button = Button(200, 245, game2_img, 1)
game3_button = Button(200, 370, game3_img, 1)

quit_button = Button(200, 495, quit_img, 1)
Main_intro_line = "게임 방법 \n\n"\
        "이동 : 화살표(↑ ↓ ← →) \n\n"\
        "일시 정지/해제 : ESC \n\n"\
        "재시작 : R \n\n"\
        "게임 종료 : E\n\n"
           
# print(pygame.font.get_fonts())
def draw_text(text, font, text_col, x, y, text_bgc = None):
    img = font.render(text, True, text_col, text_bgc)
    screen.blit(img, (x, y))

def blit_text_mulline(surface, text, pos, font, color = (0, 0, 0)):
    words = [word.split(' ') for word in text.splitlines()]
    space = font.size(' ')[0]
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, True, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]
                y += word_height
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]
        y += word_height


running = True

while running:
    screen.fill((122, 199, 82))
    pygame.draw.rect(screen, (255, 255, 255), (500, 120, 400, 450))
    draw_text("Lion Running", font1, Text_Col, 200, 0)
    blit_text_mulline(screen, Main_intro_line, (520, 150), font2)
    if game1_button.draw(screen):
        intro_1()
    
    if game2_button.draw(screen):
        intro_2()
    
    if game3_button.draw(screen):
        intro_3()
            
    if quit_button.draw(screen):
        running = False
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_e:
                running = False
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()