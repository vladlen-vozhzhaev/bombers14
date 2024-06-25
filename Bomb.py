import pygame
from configGame import *

class Bomb(pygame.sprite.Sprite):
    def __init__(self, place):
        super().__init__()
        self.image = pygame.Surface((25,25))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = place