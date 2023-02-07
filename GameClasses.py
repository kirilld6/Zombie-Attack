# Создаем класс игрока на основе pygame.sprite.Sprite
import pygame
from Constants import *


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH / 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.speed_x = 0
        self.speed_y = 0

    def update(self):
        self.speed_x = 0
        self.speed_y = 0
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.speed_x = -8
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.speed_x = 8
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.speed_y = -8
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            self.speed_y = 8
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_HEIGHT
        if self.rect.left < 0:
            self.rect.left = 0