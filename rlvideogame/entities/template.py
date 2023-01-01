import pygame


class Entity():

    def __init__(self, pos: pygame.math.Vector2) -> None:
        self._pos = pos

    @property
    def pos(self) -> pygame.math.Vector2:
        return self._pos

    def move(self, move: pygame.math.Vector2):
        self._pos += move

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 0), self._pos, 10)
