import pygame


class Snake:
    def __init__(self, body_parts, position):
        self.body_parts = body_parts
        self.position = position

    def draw_body_part(self, screen, color, position_x, position_y, size):
        pygame.draw.rect(screen, color, (position_x, position_y, size, size))
