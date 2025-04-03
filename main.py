"""
main file of the game
"""

# import modules
import pygame
import pygame_menu

# import config
import config as cg

# screen init
screen = pygame.display.set_mode((cg.SCREEN_WIDTH, cg.SCREEN_HEIGHT))
pygame.display.set_caption("Game")

# clock init
clock = pygame.time.Clock()

# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    pygame.display.flip()

    # update clock
    clock.tick(cg.FPS)

pygame.quit()
