
import math

import pygame

from rlvideogame.entities import template

def move_direction_vector(angle_degree: float) -> pygame.math.Vector2:
    angle_degree_fit = angle_degree % 360
    angle_radian = angle_degree_fit / 360 * 2 * 3.1416
    return pygame.math.Vector2(math.cos(angle_radian), math.sin(angle_radian))


def move_direction(entity: template.Entity, angle_degree: float, speed: float):
    entity.direction = entity.direction.rotate(angle_degree)
    entity.move(entity.direction * speed)