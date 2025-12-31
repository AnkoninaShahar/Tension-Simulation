import pygame
import manager

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

manager = manager.Manager()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("dark grey")

    manager.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()