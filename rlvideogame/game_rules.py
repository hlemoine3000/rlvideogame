import numpy as np


def game_of_life(grid):
    # Create a copy of the grid to store the next generation
    next_gen = np.copy(grid)

    # Iterate through each cell in the grid
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            # Count the number of live neighbors
            live_neighbors = 0
            for x in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    if x == 0 and y == 0:
                        continue
                    if (i + x >= 0 and i + x < grid.shape[0] and j + y >= 0
                            and j + y < grid.shape[1]
                            and grid[i + x][j + y] == 1):
                        live_neighbors += 1

            # Apply the rules of the Game of Life
            if grid[i][j] == 1:
                if live_neighbors < 2 or live_neighbors > 3:
                    next_gen[i][j] = 0
            else:
                if live_neighbors == 3:
                    next_gen[i][j] = 1

    # Return the next generation of the grid
    return next_gen
