import pygame
from settings import *
from objects import Tree, Grass
from character import Character
from debug import debug
from camera import CameraGroupYaxis


class Level:

    def __init__(self):

        # sprites group settings
        self.drawn_sprites = CameraGroupYaxis()  # objects with no interaction with player, like background
        self.interaction_sprites = pygame.sprite.Group()  # objects with interaction with player
        self.character = 0

        # display surface
        self.display_surface = pygame.display.get_surface()

        # map setup
        self.map_create()

    def map_create(self):

        for row_index, row in enumerate(WORLD_MAP):
            for column_index, column in enumerate(row):  # getting coordinates by rows and columns in the list
                x = column_index * TILESIZE
                y = row_index * TILESIZE

                # generating a map and giving objects their roles (no interaction or interaction)
                # idk why pycharm matching code with yellow because everything is working
                if column == 'p':
                    self.character = Character((x, y), [self.drawn_sprites], self.interaction_sprites)
                elif column == ' ':
                    Grass(pos=(x, y), groups=[self.drawn_sprites])
                elif column == 'x':
                    Tree(pos=(x, y), groups=[self.drawn_sprites, self.interaction_sprites])
                elif column == 't':
                    Tree(pos=(x, y), groups=[self.drawn_sprites, self.interaction_sprites])

    def run(self):

        # draw the game and update screen
        self.drawn_sprites.custom_object()
        self.drawn_sprites.update()






























