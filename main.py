import pygame
from configGame import *
from Player import Player
from Wall import Wall
from Bomb import Bomb
pygame.init()
background_image = pygame.image.load('img/ground/ground_05.png')
backgroundWidth, backgroundHeight = background_image.get_size()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
wall1 = Wall(100, 100)
wall2 = Wall(400, 400)
walls = pygame.sprite.Group()
walls.add(wall1, wall2)
player = Player(walls)
all_sprites.add(player, walls)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    keys = pygame.key.get_pressed()
    dx, dy = 0,0
    if keys[pygame.K_LEFT]:
        dx = -PLAYER_SPEED
    if keys[pygame.K_RIGHT]:
        dx = PLAYER_SPEED
    if keys[pygame.K_UP]:
        dy = -PLAYER_SPEED
    if keys[pygame.K_DOWN]:
        dy = PLAYER_SPEED
    if keys[pygame.K_SPACE]:
        bomb = Bomb(player.rect.center) # Создаём новую бомбу
        player.setBomb(bomb) # Попытка установить бомбу на игровом поле

    player.update(dx,dy)
    for x in range(0, SCREEN_WIDTH, backgroundWidth):
        for y in range(0, SCREEN_HEIGHT, backgroundHeight):
            screen.blit(background_image, (x,y))
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)