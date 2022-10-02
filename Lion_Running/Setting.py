import pygame   
#배경, 맵 크기 설정
BackGround_Color = (255, 255, 255)
BackGround_Img1 = pygame.image.load(".//images//bgimage1.jpg")
BackGround_Img2 = pygame.image.load(".//images//bgimage2.jpg")
BackGround_Img3 = pygame.image.load(".//images//bgimage3.jpg")
Map_width = 1100
Map_height = 700
best_score = 0
best_time = 0
#점수 생성
score = 0
#시간 카운터 생성
secs = 0
mins = 0
#소리 설정
pygame.mixer.init()
Eating_sound = pygame.mixer.Sound(".//sounds//Minecraft_Eating_-_Sound_Effect_HD.wav")
Bomb_sound = pygame.mixer.Sound(".//sounds//boom_sound_effect.wav")
Death_sound = pygame.mixer.Sound(".//sounds//Minecraft_Death_Sound_Effect.wav")
#장애물, 고기, 고슴도치 가시 설정
Map_objects = [[False for _ in range(16)] for __ in range(24)]
spawn_x_start = 1
spawn_y_start = 1
spawn_x_end = Map_width // 50 - 1
spawn_y_end = Map_height // 50 - 1
MeatNum = 10
HurdleNum = 12
bombNum = 7
pygame.init()
caption_font = pygame.font.Font("fonts\MaplestoryFont_TTF\Maplestory Bold.ttf", 50)
body_textfont = pygame.font.Font("fonts\MaplestoryFont_TTF\MapleStory Light.ttf", 30)

def is_collision_With_Lion(x1, y1, x2, y2):
    if x1 >= x2 and x1 <= x2:
        if y1 >= y2 and y1 <= y2:
            return True

    return False


#스네이크가 맵을 벗어났는지 확인하는 함수
def is_collision_Map(x, y):
    if x >= Map_width or y >= Map_height or x < 0 or y < 0:
        return True

    return False

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
