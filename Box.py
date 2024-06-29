import pygame
from configGame import *
class Box(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("img/crates/crate_42.png")
        self.image = pygame.transform.scale(self.image, (BLOCK_SIZE, BLOCK_SIZE))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y