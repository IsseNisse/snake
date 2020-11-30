import pygame
import sys
import random

pygame.init()

WIDTH = 800
HEIGHT = 500

WHITE = (255, 255, 255)
RED = (255, 0, 0)

player_pos = [400, 300]
fruit_pos = [random.randint(0, WIDTH), random.randint(0, HEIGHT)]

new_x = 10
new_y = 0

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

game_over = False

def detect_collision(player_pos, fruit_pos):
    player_x = player_pos[0]
    player_y = player_pos[1]

    fruit_x = fruit_pos[0]
    fruit_y = fruit_pos[1]

while not game_over:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                if new_x == 10:
                    new_x = 10
                    new_y = 0
                else:
                    new_x = -10
                    new_y = 0

            elif event.key == pygame.K_RIGHT:
                if new_x == -10:
                    new_x = -10
                    new_y = 0
                else:
                    new_x = 10
                    new_y = 0
            elif event.key == pygame.K_UP:
                if new_y == 10:
                    new_x = 0
                    new_y = 10
                else:
                    new_x = 0
                    new_y = -10
            elif event.key == pygame.K_DOWN:
                if new_y == -10:
                    new_x = 0
                    new_y = -10
                else:
                    new_x = 0
                    new_y = 10
            player_pos = [player_pos[0] + new_x, player_pos[1] + new_y]

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, WHITE, (player_pos[0], player_pos[1], 10, 10))
    pygame.draw.rect(screen, RED, (fruit_pos[0], fruit_pos[1], 10, 10))
    player_pos = [player_pos[0] + new_x, player_pos[1] + new_y]

    clock.tick(10)

    pygame.display.update()
