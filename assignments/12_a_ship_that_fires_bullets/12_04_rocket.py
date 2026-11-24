# Andre Pereira
# Chapter 12
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

rocket = pygame.image.load("rocket.png")
rect = rocket.get_rect()
rect.center = screen.get_rect().center

speed = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and rect.left > 0:
        rect.x -= speed
    if keys[pygame.K_RIGHT] and rect.right < 800:
        rect.x += speed
    if keys[pygame.K_UP] and rect.top > 0:
        rect.y -= speed
    if keys[pygame.K_DOWN] and rect.bottom < 600:
        rect.y += speed

    screen.fill((0, 0, 0))
    screen.blit(rocket, rect)
    pygame.display.flip()