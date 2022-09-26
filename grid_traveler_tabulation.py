def grid_traveler(target: tuple[int, int]) -> int:
    x_dim = target[0]
    y_dim = target[1]

    grid: list[list[int]] = [[0 for _ in range(0, y_dim+1)] for _ in range(0, x_dim+1)]

    if x_dim > 0 and y_dim > 0:
        grid[1][1] = 1

    for x in range(0, x_dim + 1):
        for y in range(0, y_dim + 1):
            if y < y_dim:
                grid[x][y+1] += grid[x][y]

            if x < x_dim:
                grid[x+1][y] += grid[x][y]

    return grid[x_dim][y_dim]


print(grid_traveler((0, 0)))  # 0
print(grid_traveler((1, 0)))  # 0
print(grid_traveler((0, 2)))  # 0
print(grid_traveler((1, 1)))  # 1
print(grid_traveler((2, 2)))  # 2
print(grid_traveler((3, 2)))  # 3
print(grid_traveler((10, 4)))  # 220
