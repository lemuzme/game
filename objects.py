import pygame
from settings import *


class Tree(pygame.sprite.Sprite):  # parameters for the trees

    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('pictures/tree/tree.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)


class Grass(pygame.sprite.Sprite):  # parameters for the grass(only background)

    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('pictures/tree/grass.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)

