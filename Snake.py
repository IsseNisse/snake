import pygame


class Snake:
    def __init__(self, body_parts):
        self.body_parts = body_parts

    def draw_body_part(self, screen, color, size):
        for part in self.body_parts:
            pygame.draw.rect(screen, color, (part.x, part.y, size, size))

