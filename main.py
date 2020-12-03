import time
import pygame
import sys
import random
from Snake import Snake
from body_parts import body_parts
from Powers import Powers
from Player import Player

pygame.init()

WIDTH = 800
HEIGHT = 500

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

player_size = 10

fruit_size = 10
fruit_pos = [random.randint(0, WIDTH - fruit_size), random.randint(0, HEIGHT - fruit_size)]

p1_new_x = 10
p1_new_y = 0
p2_new_x = 10
p2_new_y = 0

p1_snake_body_parts = []
p2_snake_body_parts = []
player1_obstacles = []

speed = 10

count = 0

p1_head = body_parts(400, 300)
p1_snake_body_parts.append(p1_head)
p1_snake = Snake(p1_snake_body_parts)

p2_head = body_parts(600, 300)
p2_snake_body_parts.append(p2_head)
p2_snake = Snake(p2_snake_body_parts)

my_font = pygame.font.SysFont("monospace", 25)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

player1 = Player(screen, p1_snake, WHITE, player_size)
player2 = Player(screen, p2_snake, WHITE, player_size)

powers = Powers(screen)
functions = [powers.add_cube]

clock = pygame.time.Clock()

game_over = False


def p1_detect_collision_fruit():
    player_x = p1_snake_body_parts[0].x
    player_y = p1_snake_body_parts[0].y

    fruit_x = fruit_pos[0]
    fruit_y = fruit_pos[1]

    if (player_x <= fruit_x < (player_x + player_size)) or (fruit_x <= player_x < (fruit_x + fruit_size)):
        if (player_y <= fruit_y < (player_y + player_size)) or (fruit_y <= player_y < (fruit_y + fruit_size)):
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


def draw_fruit():
    pygame.draw.rect(screen, RED, (round(fruit_pos[0], -1), round(fruit_pos[1], -1), fruit_size, fruit_size))


while not game_over:
    snake_index = 0
    flag = False
    for event in pygame.event.get():
        if not flag:
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
                flag = True

    screen.fill((0, 0, 0))

    draw_fruit()

    text = "Score: " + str(count)
    label = my_font.render(text, True, RED)
    screen.blit(label, (WIDTH - 200, HEIGHT - 40))

    # if detect_collision_snake():
    #     game_over = True

    if p1_detect_collision_fruit():
        fruit_pos = [random.randint(0, WIDTH), random.randint(0, HEIGHT)]
        draw_fruit()
        count += 1

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

    player1.move(p1_snake_body_parts, p1_new_x, p1_new_y)
    player2.move(p2_snake_body_parts, p2_new_x, p2_new_y)

    clock.tick(10)

    pygame.display.update()
