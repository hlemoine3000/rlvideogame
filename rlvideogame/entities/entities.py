import enum
import logging
import math

import pygame


berry_image = pygame.image.load('images/berry.jpg')
berry_image = pygame.transform.scale(berry_image, (20, 20))


class EntityType(enum.Enum):
    NOTHING = 1
    ITEM = 2
    CREATURE = 3


class EntityState(enum.Enum):
    DEAD = 1
    ALIVE = 2


class BaseEntity(pygame.sprite.Sprite):
    def __init__(self, pos: pygame.math.Vector2, dir: pygame.math.Vector2) -> None:
        super().__init__()

        self.entity_type = EntityType.NOTHING
        self.entiy_state = EntityState.DEAD
        self.direction = dir
        self.position = pos
        self.next_position = pos
        self.max_speed = 2.
        self.max_angle = 1. # degrees
    
    def move(self, mov: pygame.math.Vector2):
        movement = mov.copy()
        movement_distance = movement.length()
        if movement_distance > self.max_speed:
            movement_distance = self.max_speed
            movement.scale_to_length(movement_distance)
        movement_angle = movement.angle_to(self.direction) - 180
        if abs(movement_angle) > self.max_angle:
            movement = self.direction.rotate(self.max_angle) if movement_angle > 0 else self.direction.rotate(-self.max_angle)
            movement.scale_to_length(movement_distance)
        self.next_position += mov
    
    def flush_move(self):
        self.next_position = self.position

    def update(self, *args, **kwargs) -> None:
        super().update(*args, **kwargs)
        self.position = self.next_position


class Creature(BaseEntity):
    def __init__(self, pos: pygame.math.Vector2, dir: pygame.math.Vector2) -> None:
        super().__init__(pos, dir)
        self.logger = logging.getLogger(__class__.__name__)

        self.entity_type = EntityType.CREATURE
        self.entiy_state = EntityState.ALIVE

        # Set the color of the circle
        self.color = (0, 255, 0)

        # Create the image and rect attributes
        # self.image = pygame.Surface((20, 20))
        # self.image.fill((255, 255, 255))
        self.image = pygame.Surface((20, 20), pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        pygame.draw.circle(self.image, (0, 255, 0), (10, 10), 10)
        self.rect = self.image.get_rect()
        self.rect.center = self.position


    def update(self) -> None:
        self.rect.center = self.position


class Food(BaseEntity):
    def __init__(self, pos: pygame.math.Vector2, dir: pygame.math.Vector2) -> None:
        super().__init__(pos, dir)

        self.entity_type = EntityType.ITEM
        self.entiy_state = EntityState.ALIVE

        self.image = berry_image
        self.rect = self.image.get_rect()
        self.rect.move_ip(self.position)
