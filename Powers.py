from body_parts import body_parts


class Powers:
    def __init__(self, screen):
        self.screen = screen

    def double_fruit(self, player_body_parts, target_player_body_parts, new_body_pos_x, new_body_pos_y):
        player_body_parts.append(body_parts(new_body_pos_x, new_body_pos_y))
        target_player_body_parts.pop()
