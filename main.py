import pygame
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600

WHITE = (255, 255, 255)

player_pos = [400, 300]

new_x = 5
new_y = 0

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

game_over = False

while not game_over:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                if new_x == 5:
                    new_x = 5
                    new_y = 0
                else:
                    new_x = -5
                    new_y = 0

            elif event.key == pygame.K_RIGHT:
                if new_x == -5:
                    new_x = -5
                    new_y = 0
                else:
                    new_x = 5
                    new_y = 0
            elif event.key == pygame.K_UP:
                if new_y == 5:
                    new_x = 0
                    new_y = 5
                else:
                    new_x = 0
                    new_y = -5
            elif event.key == pygame.K_DOWN:
                if new_y == -5:
                    new_x = 0
                    new_y = -5
                else:
                    new_x = 0
                    new_y = 5
            player_pos = [player_pos[0] + new_x, player_pos[1] + new_y]

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, WHITE, (player_pos[0], player_pos[1], 1, 1))
    player_pos = [player_pos[0] + new_x, player_pos[1] + new_y]

    clock.tick(60)

    pygame.display.update()
