import pygame
from configGame import *

class Bomb(pygame.sprite.Sprite):
    def __init__(self, place):
        super().__init__()
        self.image = pygame.Surface((BLOCK_SIZE,BLOCK_SIZE))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        y = (place[1] + (BLOCK_SIZE - place[1]%BLOCK_SIZE)) - BLOCK_SIZE/2
        x = (place[0] + (BLOCK_SIZE - place[0]%BLOCK_SIZE)) - BLOCK_SIZE/2
        self.rect.center = (x, y)
        self.start_time = pygame.time.get_ticks()
        self.exploded = False
        self.explodeRender = True
        self.explodeX = pygame.sprite.Sprite()
        self.explodeY = pygame.sprite.Sprite()

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.start_time > 3000 and current_time - self.start_time < 3500 and not self.exploded:
            self.explodeX.image = pygame.Surface((BLOCK_SIZE + (BLOCK_SIZE*2), BLOCK_SIZE))
            self.explodeY.image = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE + (BLOCK_SIZE*2)))
            self.explodeX.image.fill(RED)
            self.explodeY.image.fill(RED)
            self.explodeX.rect = self.explodeX.image.get_rect()
            self.explodeY.rect = self.explodeY.image.get_rect()
            self.explodeX.rect.center = self.rect.center
            self.explodeY.rect.center = self.rect.center
            all_sprites.add(self.explodeX, self.explodeY)
            all_sprites.remove(self)
            self.exploded = True
        elif current_time - self.start_time > 3500 and self.explodeRender:
            all_sprites.remove(self.explodeX, self.explodeY)
            self.explodeRender = False