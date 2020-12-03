import pygame
import sys
import random
from Snake import Snake
from body_parts import body_parts

pygame.init()

WIDTH = 800
HEIGHT = 500

WHITE = (255, 255, 255)
RED = (255, 0, 0)

player_size = 10

fruit_pos = [random.randint(0, WIDTH), random.randint(0, HEIGHT)]
fruit_size = 10

new_x = 10
new_y = 0

snake_body_parts = []

speed = 10

count = 0

head = body_parts(400, 300)
snake_body_parts.append(head)
snake = Snake(snake_body_parts)

my_font = pygame.font.SysFont("monospace", 25)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

game_over = False


def detect_collision():
    player_x = snake_body_parts[0].x
    player_y = snake_body_parts[0].y

    fruit_x = fruit_pos[0]
    fruit_y = fruit_pos[1]

    if (player_x <= fruit_x < (player_x + player_size)) or (fruit_x <= player_x < (fruit_x + fruit_size)):
        if (player_y <= fruit_y < (player_y + player_size)) or (fruit_y <= player_y < (fruit_y + fruit_size)):
            return True
    return False


def draw_fruit():
    pygame.draw.rect(screen, RED, (fruit_pos[0], fruit_pos[1], fruit_size, fruit_size))


while not game_over:
    snake_index = 0
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

    screen.fill((0, 0, 0))

    draw_fruit()

    text = "Score: " + str(count)
    label = my_font.render(text, True, RED)
    screen.blit(label, (WIDTH - 200, HEIGHT - 40))

    if detect_collision():
        fruit_pos = [random.randint(0, WIDTH), random.randint(0, HEIGHT)]
        draw_fruit()
        count += 1

        i = len(snake_body_parts) - 1
        new_body_pos_x = 0
        new_body_pos_y = 0
        if new_x < 0:
            new_body_pos_x = snake_body_parts[i].x + speed
            new_body_pos_y = snake_body_parts[i].y
        elif new_x > 0:
            new_body_pos_x = snake_body_parts[i].x - speed
            new_body_pos_y = snake_body_parts[i].y
        elif new_y < 0:
            new_body_pos_y = snake_body_parts[i].y + speed
            new_body_pos_x = snake_body_parts[i].x
        elif new_y > 0:
            new_body_pos_y = snake_body_parts[i].y - speed
            new_body_pos_x = snake_body_parts[i].x

        body_part = body_parts(new_body_pos_x, new_body_pos_y)
        snake_body_parts.append(body_part)

    head = snake_body_parts[0]
    tail = snake_body_parts.pop()
    tail.x = head.x + new_x
    tail.y = head.y + new_y
    snake_body_parts.insert(0, tail)
    snake.update(snake_body_parts)

    snake.draw_body_part(screen, WHITE, player_size)

    clock.tick(10)

    pygame.display.update()
