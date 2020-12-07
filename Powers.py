<<<<<<< HEAD
from body_parts import body_parts
=======
import pygame
import random
>>>>>>> 9593256883cd1d67cc5821a314615ca1dad646ed


class Powers:
    def __init__(self, screen):
        self.screen = screen

<<<<<<< HEAD
    def double_fruit(self, player_body_parts, target_player_body_parts, new_body_pos_x, new_body_pos_y):
        player_body_parts.append(body_parts(new_body_pos_x, new_body_pos_y))
        target_player_body_parts.pop()
=======
    def add_cube(self):
        pos = [random.randint(0, 800 - 10), random.randint(0, 400 - 10)]
        return pos

    def draw_cube(self, color, pos):
        pygame.draw.rect(self.screen, color, (round(pos[0], -1), round(pos[1], -1), 10, 10))
>>>>>>> 9593256883cd1d67cc5821a314615ca1dad646ed
