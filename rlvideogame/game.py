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

        # Create the window
        self.screen = pygame.display.set_mode(screen_size)

        # Create a clock to control the frame rate
        self.clock = pygame.time.Clock()
        self.fps = fps

        self.screen_size = screen_size
        self.dot_speed = 1
        self.creature_sprites_group = pygame.sprite.Group()
        self.food_sprites_group = pygame.sprite.Group()
        self.creature_sprites_group.add(
            entities.Creature(pygame.math.Vector2(100., 100.),
            pygame.math.Vector2(1, 0))
        )
        self.creature_sprites_group.add(
            entities.Creature(pygame.math.Vector2(100., 200.),
            pygame.math.Vector2(1, 0))
        )

        self.init_events()

    def init_events(self):
        pygame.time.set_timer(Events.SPAWN_ITEMS_EVENT, 2000)

    def spawn_items(self):
        self.food_sprites_group.add(
            entities.Food(
                pygame.math.Vector2(random.randint(0, self.screen_size.x),
                                    random.randint(0, self.screen_size.y)),
                pygame.math.Vector2(0, 1)
            )
        )

    def events(self):
        for event in pygame.event.get():
            if event.type == Events.SPAWN_ITEMS_EVENT:
                self.spawn_items()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
    def update_groups(self):
        self.creature_sprites_group.update()
        self.food_sprites_group.update()

    def draw_groups(self):
        self.creature_sprites_group.draw(self.screen)
        self.food_sprites_group.draw(self.screen)

    def move(self):
        for creature_sprite in self.creature_sprites_group:
            nearest_food_vector = None
            nearest_food_distance = 1000000
            for food_sprite in self.food_sprites_group:
                creature_food_vector = food_sprite.position - creature_sprite.position
                creature_food_distance = creature_food_vector.length()
                if creature_food_distance < nearest_food_distance:
                    nearest_food_vector = creature_food_vector
                    nearest_food_distance = creature_food_distance
            if nearest_food_vector:
                creature_sprite.move(nearest_food_vector.normalize())
    
    def collision(self):
        for creature_sprite in self.creature_sprites_group:
            food_collide_group = pygame.sprite.spritecollide(creature_sprite, self.food_sprites_group, False, pygame.sprite.collide_rect)
            for food_collide_sprite in food_collide_group:
                food_collide_sprite.kill()

    def game_loop(self):

        # Run the game loop
        while True:
            # Clear the screen
            self.screen.fill((255, 255, 255))
            
            # Handle events
            self.events()
            self.move()
            self.collision()
            self.update_groups()
            self.draw_groups()

            # Update the display
            pygame.display.flip()

            # Limit the frame rate to the specified value
            self.clock.tick(self.fps)


def game():

    random.seed(1)
    logging.config.fileConfig(fname='logging.conf', disable_existing_loggers=False)

    # Initialize pygame
    pygame.init()

    my_world = Wolrd(pygame.math.Vector2(1600, 1000), 120)
    my_world.game_loop()
