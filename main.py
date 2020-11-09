import pygame
import os

os.environ['SDL_VIDEO_CENTERED'] = '1'

WIDTH_WIN, HEIGHT_WIN = 800, 800
collide = False
collide2 = False


rect_size = w, h = 250, 250
rect_pos = ((WIDTH_WIN - w) // 2, (HEIGHT_WIN - h) // 2)

circle_radius = 55
circle_pos = (0, 0)

FPS = 120
RED = (255, 0, 0, 180)
BLUE = (0, 0, 255, 180)
YELLOW = (255, 255, 0, 180)
BG = (128, 128, 128)
x = 0
y = 0
block = False
speed_x, speed_y = 5, 4
ball = pygame.image.load('image/ball.png')
ball_rect = ball.get_rect()
print(ball_rect)

pygame.init()
pygame.display.set_caption('DRAW and COLLIDE')
screen = pygame.display.set_mode((WIDTH_WIN, HEIGHT_WIN))
font = pygame.font.SysFont('Arial', 24, True, False)
clock = pygame.time.Clock()

surface = pygame.Surface((circle_radius * 2, circle_radius * 2), pygame.SRCALPHA)
pygame.draw.circle(surface, YELLOW, (circle_radius, circle_radius), circle_radius)
rect1 = surface.get_rect()

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT or \
            e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            run = False
        elif e.type == pygame.MOUSEMOTION:
            circle_pos = e.pos
            rect1_center = e.pos

    ball_rect = ball_rect.move(speed_x, speed_y)
    if ball_rect.left < 0 or ball_rect.right > WIDTH_WIN:
        speed_x = -speed_x
    if ball_rect.top < 0 or ball_rect.bottom > HEIGHT_WIN:
        speed_y = -speed_y

    screen.fill(BG)
    COLOR = RED if collide else BLUE

    rect1 = pygame.draw.circle(screen, YELLOW, circle_pos, circle_radius)
    rect2 = pygame.draw.rect(screen, RED if collide else BLUE, (rect_pos, rect_size))

    if ball_rect.colliderect(rect2):
        collide = True
        if COLOR == BLUE:
            y += 1
    elif rect1.colliderect(rect2):
        collide = True
        if COLOR == BLUE:
            x += 1
    else:
        collide = False

    

    #ball_rect.x += 1
    #ball_rect.y += 1
    ball_rect = ball_rect.move(speed_x, speed_y)
    #ball_rect.centerx += 1

    screen.blit(surface, rect1)
    screen.blit(ball, ball_rect)
    screen.blit(font.render(str(x), 1, RED), (10,10))
    screen.blit(font.render(str(y), 1, RED), (WIDTH_WIN-100,10))
    pygame.display.update()
    clock.tick(FPS)
   
