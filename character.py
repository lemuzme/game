import pygame
from settings import *


class Character(pygame.sprite.Sprite):

    def __init__(self, pos, groups, interaction_sprites):

        # constants and parameters
        super().__init__(groups)
        self.image = pygame.image.load('pictures/characters/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.speed = 5
        self.coordinates_changes = pygame.math.Vector2()
        self.interaction_sprites = interaction_sprites

    def input(self): # getting what key is pressed and how coordinates are changing

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.coordinates_changes.y = -1
        elif keys[pygame.K_s]:
            self.coordinates_changes.y = 1
        else:
            self.coordinates_changes.y = 0

        if keys[pygame.K_a]:
            self.coordinates_changes.x = -1
        elif keys[pygame.K_d]:
            self.coordinates_changes.x = 1
        else:
            self.coordinates_changes.x = 0

    def movements(self, speed):  # player coordinates changing
        if self.coordinates_changes.magnitude() != 0:
            self.coordinates_changes = self.coordinates_changes.normalize()
        self.rect.x += self.coordinates_changes.x * speed
        self.collision('horizontal')  # left and right collisions
        self.rect.y += self.coordinates_changes.y * speed
        self.collision('vertical')  # top and bottom collisions

    def collision(self, coordinates_changes):  # player with objects interaction
        if coordinates_changes == 'horizontal':
            for sprite in self.interaction_sprites:
                if sprite.rect.colliderect(self.rect):  # checking the collision
                    if self.coordinates_changes.x > 0:  # if player moving right the collision should be with right side
                        self.rect.right = sprite.rect.left
                    if self.coordinates_changes.x < 0:  # if player moving left the collision should be with left side
                        self.rect.left = sprite.rect.right

        if coordinates_changes == 'vertical':
            for sprite in self.interaction_sprites:
                if sprite.rect.colliderect(self.rect):  # checking the collision
                    if self.coordinates_changes.y < 0:  # if player moving up the collision should be with top
                        self.rect.top = sprite.rect.bottom
                    if self.coordinates_changes.y > 0:  # if player moving down the collision should be with bottom
                        self.rect.bottom = sprite.rect.top

    def update(self):
        self.movements(self.speed)
        self.input()
