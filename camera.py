import pygame
from settings import *
from objects import Tree, Grass
from character import Character
from debug import debug


class CameraGroupYaxis(pygame.sprite.Group):

    def __init__(self):

        # general setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()

    def custom_object(self):
        for sprite in self.sprites():
            self.display_surface.blit(sprite.image, sprite.rect)
