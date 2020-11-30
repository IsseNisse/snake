import pygame
import sys
import random

pygame.init()

WIDTH = 800
HEIGHT = 500

WHITE = (255, 255, 255)
RED = (255, 0, 0)

player_pos = [400, 300]
player_size = 10

fruit_pos = [random.randint(0, WIDTH), random.randint(0, HEIGHT)]
fruit_size = 10

new_x = 10
new_y = 0

speed = 10

count = 0

my_font = pygame.font.SysFont("monospace", 25)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

snake = [1, 2, 3]

game_over = False


def detect_collision():
    player_x = player_pos[0]
    player_y = player_pos[1]

    fruit_x = fruit_pos[0]
    fruit_y = fruit_pos[1]

    if (player_x <= fruit_x < (player_x + player_size)) or (fruit_x <= player_x < (fruit_x + fruit_size)):
        if (player_y <= fruit_y < (player_y + player_size)) or (fruit_y <= player_y < (fruit_y + fruit_size)):
            return True
    return False


def draw_fruit():
    pygame.draw.rect(screen, RED, (fruit_pos[0], fruit_pos[1], fruit_size, fruit_size))


def draw_snake():
    pygame.draw.rect(screen, WHITE, (player_pos[0], player_pos[1], player_size, player_size))


while not game_over:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                if new_x == speed:
                    new_x = speed
                    new_y = 0
                else:
                    new_x = -speed
                    new_y = 0

            elif event.key == pygame.K_RIGHT:
                if new_x == -speed:
                    new_x = -speed
                    new_y = 0
                else:
                    new_x = speed
                    new_y = 0
            elif event.key == pygame.K_UP:
                if new_y == speed:
                    new_x = 0
                    new_y = speed
                else:
                    new_x = 0
                    new_y = -speed
            elif event.key == pygame.K_DOWN:
                if new_y == -speed:
                    new_x = 0
                    new_y = -speed
                else:
                    new_x = 0
                    new_y = speed
            player_pos = [player_pos[0] + new_x, player_pos[1] + new_y]

    screen.fill((0, 0, 0))

    draw_fruit()

    text = "Score: " + str(count)
    label = my_font.render(text, True, RED)
    screen.blit(label, (WIDTH - 200, HEIGHT - 40))

    if detect_collision():
        fruit_pos = [random.randint(0, WIDTH), random.randint(0, HEIGHT)]
        draw_fruit()
        count += 1
        snake.append(count)

    for i in range(len(snake)):
        added_part_x = player_pos[0] + 5
        added_part_y = player_pos[1] + 5
        draw_snake(added_part_x, added_part_y)

    player_pos = [player_pos[0] + new_x, player_pos[1] + new_y]

    clock.tick(10)

    pygame.display.update()
