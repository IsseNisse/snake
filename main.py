import time
import pygame
import sys
import random
from Snake import Snake
from body_parts import body_parts
from Powers import Powers
from Player import Player
from pygame.locals import *

pygame.init()

WIDTH = 960
HEIGHT = 960
WIDTH_HALF = WIDTH/2 - 5

screen = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

player_size = 10

fruit_size = 10
p1_fruit_pos = [round(random.randint(fruit_size, WIDTH_HALF - fruit_size), -1), round(random.randint(fruit_size, HEIGHT - fruit_size), -1)]
p2_fruit_pos = [round(random.randint(WIDTH_HALF, WIDTH - fruit_size), -1), round(random.randint(fruit_size, HEIGHT - fruit_size), -1)]

p1_new_x = 10
p1_new_y = 0
p2_new_x = 10
p2_new_y = 0

p1_snake_body_parts = []
p2_snake_body_parts = []
p1_obstacles = []
p2_obstacles = []

speed = 10

p1_count = 0
p2_count = 0

p1_head = body_parts(100, 300)
p1_snake_body_parts.append(p1_head)
p1_snake = Snake(p1_snake_body_parts)

p2_head = body_parts(600, 300)
p2_snake_body_parts.append(p2_head)
p2_snake = Snake(p2_snake_body_parts)

my_font = pygame.font.SysFont("monospace", 25)

player1 = Player(screen, p1_snake, WHITE, player_size)
player2 = Player(screen, p2_snake, WHITE, player_size)

powers = Powers(screen)
functions = [powers.add_cube]

clock = pygame.time.Clock()

game_over = False


def detect_collision_fruit(snake_body_parts, fruit_pos):
    player_x = snake_body_parts[0].x
    player_y = snake_body_parts[0].y

    fruit_x = fruit_pos[0]
    fruit_y = fruit_pos[1]

    if (player_x <= fruit_x < (player_x + player_size)) or (fruit_x <= player_x < (fruit_x + fruit_size)):
        if (player_y <= fruit_y < (player_y + player_size)) or (fruit_y <= player_y < (fruit_y + fruit_size)):
            return True
    return False


def detect_collision_wall(snake_body_parts, width, height):
    player_x = snake_body_parts[0].x
    player_y = snake_body_parts[0].y

    wall_x = width
    wall_y = height

    if (player_x <= wall_x < (player_x + player_size)) or (wall_x <= player_x < (wall_x + 10)):
        if (player_y <= wall_y < (player_y + player_size)) or (wall_y <= player_y < (wall_y + 10)):
            return True
    return False


# def detect_collision_snake():
#     for j in range(2, len(snake_body_parts)):
#
#         player_x = snake_body_parts[0].x
#         player_y = snake_body_parts[0].y
#
#         body_x = snake_body_parts[j].x
#         body_y = snake_body_parts[j].y
#
#         if body_x <= player_x <= body_x + player_size:
#             if body_y <= player_y <= body_y + player_size:
#                 return True
#         return False


def draw_fruit(fruit_pos):
    pygame.draw.rect(screen, RED, (round(fruit_pos[0], -1), round(fruit_pos[1], -1), fruit_size, fruit_size))


while not game_over:
    snake_index = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            start_timer = pygame.time.get_ticks()
            if event.key == pygame.K_LEFT:
                if p1_new_x == speed:
                    p1_new_x = speed
                    p1_new_y = 0
                else:
                    p1_new_x = -speed
                    p1_new_y = 0

            elif event.key == pygame.K_RIGHT:
                if p1_new_x == -speed:
                    p1_new_x = -speed
                    p1_new_y = 0
                else:
                    p1_new_x = speed
                    p1_new_y = 0
            elif event.key == pygame.K_UP:
                if p1_new_y == speed:
                    p1_new_x = 0
                    p1_new_y = speed
                else:
                    p1_new_x = 0
                    p1_new_y = -speed
            elif event.key == pygame.K_DOWN:
                if p1_new_y == -speed:
                    p1_new_x = 0
                    p1_new_y = -speed
                else:
                    p1_new_x = 0
                    p1_new_y = speed
            if event.key == pygame.K_a:
                if p2_new_x == speed:
                    p2_new_x = speed
                    p2_new_y = 0
                else:
                    p2_new_x = -speed
                    p2_new_y = 0

            elif event.key == pygame.K_d:
                if p2_new_x == -speed:
                    p2_new_x = -speed
                    p2_new_y = 0
                else:
                    p2_new_x = speed
                    p2_new_y = 0
            elif event.key == pygame.K_w:
                if p2_new_y == speed:
                    p2_new_x = 0
                    p2_new_y = speed
                else:
                    p2_new_x = 0
                    p2_new_y = -speed
            elif event.key == pygame.K_s:
                if p2_new_y == -speed:
                    p2_new_x = 0
                    p2_new_y = -speed
                else:
                    p2_new_x = 0
                    p2_new_y = speed

    screen.fill((0, 0, 0))

    draw_fruit(p1_fruit_pos)
    draw_fruit(p2_fruit_pos)

    p2_text = "Player 2 Score: " + str(p1_count)
    p2_label = my_font.render(p2_text, True, RED)
    screen.blit(p2_label, (WIDTH_HALF + 40, HEIGHT - 40))
    p1_text = "Player 1 Score: " + str(p1_count)
    p1_label = my_font.render(p1_text, True, RED)
    screen.blit(p1_label, (40, HEIGHT - 40))

    # if detect_collision_snake():
    #     game_over = True

    if detect_collision_fruit(p1_snake_body_parts, p1_fruit_pos):
        p1_fruit_pos = [round(random.randint(fruit_size, WIDTH_HALF - fruit_size), -1), round(random.randint(fruit_size, HEIGHT - fruit_size), -1)]
        for i in range(len(p1_obstacles)):
            if p1_fruit_pos == p1_obstacles[i]:
                p1_fruit_pos = [round(random.randint(fruit_size, WIDTH_HALF - fruit_size), -1), round(random.randint(fruit_size, HEIGHT - fruit_size), -1)]
        draw_fruit(p1_fruit_pos)
        p1_count += 1

        i = len(p1_snake_body_parts) - 1
        new_body_pos_x = 0
        new_body_pos_y = 0
        if p1_new_x < 0:
            new_body_pos_x = p1_snake_body_parts[i].x + speed
            new_body_pos_y = p1_snake_body_parts[i].y
        elif p1_new_x > 0:
            new_body_pos_x = p1_snake_body_parts[i].x - speed
            new_body_pos_y = p1_snake_body_parts[i].y
        elif p1_new_y < 0:
            new_body_pos_y = p1_snake_body_parts[i].y + speed
            new_body_pos_x = p1_snake_body_parts[i].x
        elif p1_new_y > 0:
            new_body_pos_y = p1_snake_body_parts[i].y - speed
            new_body_pos_x = p1_snake_body_parts[i].x

        body_part = body_parts(new_body_pos_x, new_body_pos_y)
        p1_snake_body_parts.append(body_part)

        cube_pos = [round(random.randint(WIDTH_HALF, WIDTH), -1), round(random.randint(0, HEIGHT), -1)]
        p2_obstacles.append(cube_pos)

    elif detect_collision_fruit(p2_snake_body_parts, p2_fruit_pos):
        p2_fruit_pos = [round(random.randint(WIDTH_HALF, WIDTH - fruit_size), -1), round(random.randint(fruit_size, HEIGHT - fruit_size), -1)]
        draw_fruit(p2_fruit_pos)
        p2_count += 1

        i = len(p2_snake_body_parts) - 1
        new_body_pos_x = 0
        new_body_pos_y = 0
        if p2_new_x < 0:
            new_body_pos_x = p2_snake_body_parts[i].x + speed
            new_body_pos_y = p2_snake_body_parts[i].y
        elif p2_new_x > 0:
            new_body_pos_x = p2_snake_body_parts[i].x - speed
            new_body_pos_y = p2_snake_body_parts[i].y
        elif p2_new_y < 0:
            new_body_pos_y = p2_snake_body_parts[i].y + speed
            new_body_pos_x = p2_snake_body_parts[i].x
        elif p2_new_y > 0:
            new_body_pos_y = p2_snake_body_parts[i].y - speed
            new_body_pos_x = p2_snake_body_parts[i].x

        body_part = body_parts(new_body_pos_x, new_body_pos_y)
        p2_snake_body_parts.append(body_part)

        cube_pos = [round(random.randint(fruit_size, WIDTH_HALF), -1), round(random.randint(0, HEIGHT), -1)]
        p1_obstacles.append(cube_pos)
    for i in range(len(p1_obstacles)):
        if detect_collision_wall(p1_snake_body_parts, p1_obstacles[i][0], p1_obstacles[i][1]):
            game_over = True

    for i in range(len(p2_obstacles)):
        if detect_collision_wall(p2_snake_body_parts, p2_obstacles[i][0], p2_obstacles[i][1]):
            game_over = True

    if p1_snake_body_parts[0].x < 10:
        if p1_new_x < 0:
            p1_snake_body_parts[0].x = WIDTH_HALF - (player_size * 2)
        elif p1_new_x > 0:
            p1_snake_body_parts[0].x = 0
    if p1_snake_body_parts[0].y < 0:
        if p1_new_y < 0:
            p1_snake_body_parts[0].y = HEIGHT
        elif p1_new_y > 0:
            p1_snake_body_parts[0].y = 0
    if p1_snake_body_parts[0].x > WIDTH_HALF - player_size * 2:
        if p1_new_x < 0:
            p1_snake_body_parts[0].x = WIDTH_HALF
        elif p1_new_x > 0:
            p1_snake_body_parts[0].x = 0
    if p1_snake_body_parts[0].y > HEIGHT:
        if p1_new_y < 0:
            p1_snake_body_parts[0].y = HEIGHT
        elif p1_new_y > 0:
            p1_snake_body_parts[0].y = 0

    if p2_snake_body_parts[0].x < WIDTH_HALF + player_size:
        if p2_new_x < 0:
            p2_snake_body_parts[0].x = WIDTH - (player_size * 2)
        elif p2_new_x > 0:
            p2_snake_body_parts[0].x = WIDTH_HALF + player_size
    if p2_snake_body_parts[0].y < 0:
        if p2_new_y < 0:
            p2_snake_body_parts[0].y = HEIGHT
        elif p2_new_y > 0:
            p2_snake_body_parts[0].y = 0
    if p2_snake_body_parts[0].x > WIDTH - player_size * 2:
        if p2_new_x < 0:
            p2_snake_body_parts[0].x = WIDTH
        elif p2_new_x > 0:
            p2_snake_body_parts[0].x = WIDTH_HALF + player_size
    if p2_snake_body_parts[0].y > 950:
        if p2_new_y < 0:
            p2_snake_body_parts[0].y = HEIGHT
        elif p2_new_y > 0:
            p2_snake_body_parts[0].y = 0

    for i in range(HEIGHT):
        pygame.draw.rect(screen, BLUE, (WIDTH_HALF, i * 10, 5, 5))

    for i in range(len(p1_obstacles)):
        powers.draw_cube(GREEN, p1_obstacles[i])

    for i in range(len(p2_obstacles)):
        powers.draw_cube(YELLOW, p2_obstacles[i])

    player1.move(p1_snake_body_parts, p1_new_x, p1_new_y)
    player2.move(p2_snake_body_parts, p2_new_x, p2_new_y)

    clock.tick(10)

    pygame.display.update()
