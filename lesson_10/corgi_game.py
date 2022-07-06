import pygame
from pygame.locals import *
import random

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont("MS Comic Sans", 30)

clock = pygame.time.Clock()

window_width = 1000
window_height = 600
velocity = 20

window = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("HArdCoder game")

RED, GREEN, BLUE, WHITE = (255,0,0), (0,255,0), (0,0,255), (255,255,255)
BLACK = (0,0,0)

player_width, player_height = 100, 100
meat_width, meat_height =  50, 50

player = pygame.Rect(250, 500, player_width, player_height)
balls = []
points = 0

pygame.mixer.music.load("mario.mid")
pygame.mixer.music.play(-1, 0.0)

player_img = pygame.image.load("corgi.png")
player_img = pygame.transform.scale(player_img, (player_width, player_height))
meat_img = pygame.image.load("meat.png")
meat_img = pygame.transform.scale(meat_img, (meat_width, meat_height))
bg_img = pygame.image.load("idylla.png")
bg_img = pygame.transform.scale(bg_img, (window_width, window_height))

action_sound = pygame.mixer.Sound("item.wav")

while True:
    window.blit(bg_img, (0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and player.left > 0:
        player.left -= velocity
    if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and player.right < window_width:
        player.right += velocity
    if keys[pygame.K_SPACE]:
        new_ball = pygame.Rect(random.randint(0,window_width), 0, meat_width, meat_height)
        balls.append(new_ball)

#    pygame.draw.rect(window, RED, player)

    window.blit(player_img, player)

    for ball in balls[:]:
        ball.bottom += 10
        if player.colliderect(ball):
           points += 1
           balls.remove(ball)
           action_sound.play()
        elif ball.bottom>= window_height:
            points -= 1
            balls.remove(ball)
        else:
 #           pygame.draw.rect(window, GREEN, ball)
            window.blit(meat_img, ball)

    #print(points)
    points_text = myfont.render("POINTS: " + str(points), False, WHITE)
    window.blit(points_text, (window_width*0.1, window_height-100))
    pygame.display.update()
    clock.tick(10)