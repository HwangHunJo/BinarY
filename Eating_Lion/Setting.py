import pygame   
#배경, 맵 크기 설정
BackGround_Color = (255, 255, 255) # 배경 색깔을 하얀색으로 설정
BackGround_Img1 = pygame.image.load(".//images//bgimage1.jpg")
BackGround_Img2 = pygame.image.load(".//images//bgimage2.jpg")
BackGround_Img3 = pygame.image.load(".//images//bgimage3.jpg")
GameOver_Img = pygame.image.load(".//images//game_over.png")
GameOver_Img.set_alpha(50)
Map_width = 1100 # 맵의 가로
Map_height = 700 # 맵의 세로
best_score = 0
#소리 설정
pygame.mixer.init()
Eating_sound = pygame.mixer.Sound(".//sounds//Minecraft_Eating_-_Sound_Effect_HD.wav") # 고기를 먹었을때
Thorn_sound = pygame.mixer.Sound(".//sounds//boom_sound_effect.wav") # 가시에 닿아서 죽었을때
Death_sound = pygame.mixer.Sound(".//sounds//Minecraft_Death_Sound_Effect.wav") # 죽었을때
#장애물, 고기, 고슴도치 가시 설정
Map_objects = [[False for _ in range(16)] for __ in range(24)] # 맵을 확인하는 배열
spawn_x_start = 1 # 고기, 장애물, 고슴도치 생성의 x축 시작 범위 
spawn_x_end = Map_width // 50 - 1 # 고기, 장애물, 고슴도치 생성의 x축 끝 범위 
spawn_y_start = 1 # 고기, 장애물, 고슴도치 생성의 y축 시작 범위 
spawn_y_end = Map_height // 50 - 1 # 고기, 장애물, 고슴도치 생성의 x축 끝 범위 
MeatNum = 10 # 고기 개수
HurdleNum = 12 # 장애물 개수
ThornNum = 7 # 가시 개수
pygame.font.init() # 폰트를 불러오기 위해 pygame.font.init() 실행
caption_font = pygame.font.Font("fonts\MaplestoryFont_TTF\Maplestory Bold.ttf", 50) # 제목에 쓸 폰트 불러오기
body_textfont = pygame.font.Font("fonts\MaplestoryFont_TTF\MapleStory Light.ttf", 30) # 본문에 쓸 폰트 불러오기


def is_collision_Map(x, y): # 맵을 벗어났는지 확인하는 함수
    if x >= Map_width or y >= Map_height or x < 0 or y < 0: # 맵을 벗어났다면
        # x가 화면의 오른쪽(Map_width)이상이거나 0보다 작거나 y가 화면의 위(Map_height)이상이거나 0보다 작을때
        return True # True를 return

    return False # False를 return

def blit_text_mulline(surface, text, pos, font, color = (0, 0, 0)): # 화면 여러줄에 글자를 표시
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
