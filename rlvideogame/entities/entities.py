import enum
import logging

import pygame


berry_image = pygame.image.load('images/berry.jpg')
berry_image = pygame.transform.scale(berry_image, (20, 20))


class EntityType(enum.Enum):
    ITEM = 1
    CREATURE = 2


class Creature(pygame.sprite.Sprite):
    def __init__(self, pos: pygame.math.Vector2, dir: pygame.math.Vector2):
        super().__init__()
        self.logger = logging.getLogger(__class__.__name__)

        self.entity_type = EntityType.CREATURE
        self.direction = dir
        self.position = pos

        # Set the color of the circle
        self.color = (0, 255, 0)

        # Create the image and rect attributes
        self.image = pygame.Surface((20, 20))
        self.image.fill((255, 255, 255))
        pygame.draw.circle(self.image, (0, 255, 0), (10, 10), 10)
        self.rect = self.image.get_rect()
        self.rect.center = self.position
    
    def update(self) -> None:
        self.direction.rotate_ip(1)
        self.position += self.direction
        self.rect.center = self.position


class Food(pygame.sprite.Sprite):
    def __init__(self, pos: pygame.math.Vector2, dir: pygame.math.Vector2):
        super().__init__()

        self.entity_type = EntityType.ITEM
        self.direction = dir

        self.image = berry_image
        self.rect = self.image.get_rect()
        self.rect.move_ip(pos)
