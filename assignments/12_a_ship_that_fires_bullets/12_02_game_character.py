# Andre Pereira
# Chapter 12

import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game Character")

class Character:
    def __init__(self):
        self.image = pygame.image.load("character.bmp")
        self.rect = self.image.get_rect()
        self.rect.center = screen.get_rect().center

    def draw(self):
        screen.blit(self.image, self.rect)

character = Character()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()