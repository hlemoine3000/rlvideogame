import pygame


class Entity():

    def __init__(self, pos: pygame.math.Vector2, dir: pygame.math.Vector2) -> None:
        self._pos = pos
        if not dir.is_normalized:
            raise ValueError('direction vector must be normalized')
        self._dir = dir

    @property
    def position(self) -> pygame.math.Vector2:
        return self._pos

    @property
    def direction(self) -> pygame.math.Vector2:
        return self._dir
    
    @direction.setter
    def direction(self, val: pygame.math.Vector2):
        if type(val) is not pygame.math.Vector2:
            return ValueError('direction must be a Vector2')
        if not val.is_normalized:
            raise ValueError('direction vector must be normalized')
        self._dir = val

    def move(self, move: pygame.math.Vector2):
        self._pos += move

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 0), self._pos, 10)
