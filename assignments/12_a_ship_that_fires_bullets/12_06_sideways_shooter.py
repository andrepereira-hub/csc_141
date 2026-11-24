# Andre Pereira
# Chapter 12

import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

ship = pygame.image.load("rocket.png")
ship_rect = ship.get_rect()
ship_rect.left = 10
ship_rect.centery = 300

bullets = []
speed = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = pygame.Rect(ship_rect.right, ship_rect.centery - 2, 10, 4)
                bullets.append(bullet)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and ship_rect.top > 0:
        ship_rect.y -= speed
    if keys[pygame.K_DOWN] and ship_rect.bottom < 600:
        ship_rect.y += speed

    for bullet in bullets:
        bullet.x += 8

    bullets = [bullet for bullet in bullets if bullet.left < 800]

    screen.fill((0, 0, 0))
    screen.blit(ship, ship_rect)

    for bullet in bullets:
        pygame.draw.rect(screen, (255, 255, 255), bullet)

    pygame.display.flip()