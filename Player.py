class Player:
    def __init__(self, screen, snake, color, player_size):
        self.screen = screen
        self.snake = snake
        self.color = color
        self.player_size = player_size

    def move(self, snake_body_parts, new_x, new_y):
        head = snake_body_parts[0]
        tail = snake_body_parts.pop()
        tail.x = head.x + new_x
        tail.y = head.y + new_y
        snake_body_parts.insert(0, tail)
        self.snake.update(snake_body_parts)
        self.snake.draw_body_part(self.screen, self.color, self.player_size)
