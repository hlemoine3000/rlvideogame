import sys

import pygame

from rlvideogame.entities import template
from rlvideogame.entities import move


class Wolrd():

    def __init__(self, screen_size: pygame.math.Vector2) -> None:
        self.screen_size = screen_size
        self.dot_speed = 1
        self.creatures_list = [
            template.Entity(pygame.math.Vector2(100., 100.), pygame.math.Vector2(1, 0)),
            template.Entity(pygame.math.Vector2(100., 200.), pygame.math.Vector2(1, 0)),
            template.Entity(pygame.math.Vector2(200., 200.), pygame.math.Vector2(1, 0)),
            template.Entity(pygame.math.Vector2(200., 100.), pygame.math.Vector2(1, 0)),
        ]

        # Create the window
        self.screen = pygame.display.set_mode(screen_size)

    def entities_move(self):
        for entity in self.creatures_list:
            move.move_direction(entity, 1, 1)
    
    def entities_draw(self):
        for entity in self.creatures_list:
            entity.draw(self.screen)

    def update(self):

        # Clear the screen
        self.screen.fill((255, 255, 255))

        move_vector = pygame.math.Vector2(0, 0)
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_UP:
            #         move_vector.y -= self.dot_speed
            #     elif event.key == pygame.K_DOWN:
            #         move_vector.y += self.dot_speed
            #     elif event.key == pygame.K_LEFT:
            #         move_vector.x -= self.dot_speed
            #     elif event.key == pygame.K_RIGHT:
            #         move_vector.x += self.dot_speed

        self.entities_move()
        self.entities_draw()

        # Update the display
        pygame.display.flip()


def game():

    my_world = Wolrd(pygame.math.Vector2(800, 800))

    # Initialize pygame
    pygame.init()

    # Create a clock to control the frame rate
    clock = pygame.time.Clock()

    # Run the game loop
    while True:
        my_world.update()

        # Limit the frame rate to the specified value
        clock.tick(120)
