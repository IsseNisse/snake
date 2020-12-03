import pygame


class Powers:

    def __init__(self, screen):
        self.screen = screen

    def change_speed(self, player_1, player_2, speed, timer):
        if player_1 == player_2:
            player_1.speed = speed / 2
            player_1.timer = timer
        elif player_2 == player_1:
            player_2.speed = speed / 2
            player_2.timer = timer

