import pygame
import random


class Powers:
    def __init__(self, screen):
        self.screen = screen

    def add_cube(self):
        pos = [random.randint(0, 800 - 10), random.randint(0, 400 - 10)]
        return pos

    def draw_cube(self, color):
        pygame.draw.rect(self.screen, color, (round(pos[0], -1), round(pos[1], -1), 10, 10))
