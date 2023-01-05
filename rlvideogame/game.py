import logging
import logging.config
import random
import sys

import pygame

from rlvideogame.entities import entities

# Events
class Events():
    SPAWN_ITEMS_EVENT = pygame.USEREVENT + 1


class Wolrd():

    def __init__(self, screen_size: pygame.math.Vector2, fps: int) -> None:

        self.logger = logging.getLogger(__class__.__name__)

        # Create a clock to control the frame rate
        self.clock = pygame.time.Clock()
        self.fps = fps

        self.screen_size = screen_size
        self.dot_speed = 1
        self.sprites_group = pygame.sprite.Group()
        self.sprites_group.add(
            entities.Creature(pygame.math.Vector2(100., 100.),
            pygame.math.Vector2(1, 0))
        )
        self.sprites_group.add(
            entities.Creature(pygame.math.Vector2(100., 200.),
            pygame.math.Vector2(1, 0))
        )

        # Create the window
        self.screen = pygame.display.set_mode(screen_size)

        self.init_events()

    def init_events(self):
        pygame.time.set_timer(Events.SPAWN_ITEMS_EVENT, 10000)

    def spawn_items(self):
        self.sprites_group.add(
            entities.Food(
                pygame.math.Vector2(random.randint(0, self.screen_size.x),
                                    random.randint(0, self.screen_size.y)),
                pygame.math.Vector2(0, 1)
            )
        )

    def events(self):
        for event in pygame.event.get():
            if event.type == Events.SPAWN_ITEMS_EVENT:
                self.logger.debug("Spawn event")
                self.spawn_items()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        

    def game_loop(self):

        # Initialize pygame
        self.logger.debug("Init PyGame")
        pygame.init()

        # Run the game loop
        while True:
            # Clear the screen
            self.screen.fill((255, 255, 255))
            
            # Handle events
            self.events()
            self.sprites_group.update()
            self.sprites_group.draw(self.screen)

            # Update the display
            pygame.display.flip()

            # Limit the frame rate to the specified value
            self.clock.tick(self.fps)


def game():

    random.seed(1)
    logging.config.fileConfig(fname='logging.conf', disable_existing_loggers=False)

    my_world = Wolrd(pygame.math.Vector2(1600, 1000), 120)
    my_world.game_loop()
