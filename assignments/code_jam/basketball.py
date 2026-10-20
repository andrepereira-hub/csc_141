# Andre Pereira
# pygame
import random
import pygame
pygame.init()
clock = pygame.time.Clock()
img_rect = pygame.image.load("assignments/code_jam/images/basketball.png")
img = pygame.image.load("assignments/code_jam/images/basketball.png")
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
img_rect = img.get_rect()


img_rect.x = random.randint(0, WIDTH - img_rect.width)
img_rect.y = random.randint(0, HEIGHT - img_rect.height)


running = True
while running:
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        
        img_rect.x = random.randint(0, WIDTH - img_rect.width)
        img_rect.y = random.randint(0, HEIGHT - img_rect.height)
       
        screen.fill((0, 0, 0))
        screen.blit(source=img, dest=img_rect)
        pygame.display.flip()
        clock.tick(5)