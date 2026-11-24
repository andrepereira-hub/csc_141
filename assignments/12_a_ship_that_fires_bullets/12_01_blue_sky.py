# Andre Pereira
# Chapter 12

import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Blue Sky")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((0, 0, 255))
    pygame.display.flip()