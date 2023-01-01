import sys

import pygame

from rlvideogame.entities import template


class Wolrd():

    def __init__(self, screen_size: tuple = (400, 400)) -> None:
        self.screen_size = screen_size
        self.dot_speed = 1
        self.creatures_list = [
            template.Entity(pygame.math.Vector2(100, 100)),
            template.Entity(pygame.math.Vector2(100, 200)),
            template.Entity(pygame.math.Vector2(200, 200)),
            template.Entity(pygame.math.Vector2(200, 100)),
        ]

        # Create the window
        self.screen = pygame.display.set_mode(screen_size)

    def update(self):

        # Clear the screen
        self.screen.fill((255, 255, 255))

        move_vector = pygame.math.Vector2(0, 0)
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    move_vector.y -= self.dot_speed
                elif event.key == pygame.K_DOWN:
                    move_vector.y += self.dot_speed
                elif event.key == pygame.K_LEFT:
                    move_vector.x -= self.dot_speed
                elif event.key == pygame.K_RIGHT:
                    move_vector.x += self.dot_speed

        # Draw the dot
        for entity in self.creatures_list:
            entity.move(move_vector)
            entity.draw(self.screen)

        # Update the display
        pygame.display.flip()


def game():

    my_world = Wolrd()

    # Initialize pygame
    pygame.init()

    # Run the game loop
    while True:
        my_world.update()
