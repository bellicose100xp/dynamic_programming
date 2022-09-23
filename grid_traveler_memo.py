def grid_traveler(init_pos: tuple[int, int], memo: dict[str, int] = {}) -> int:
    x = init_pos[0]
    y = init_pos[1]

    if x == 0 or y == 0:
        return 0

    if (x, y) == (1, 1):
        return 1
    
    key: str = f'${x},${y}'

    if key in memo:
        return memo[key]
    else:
        memo[key] = grid_traveler((x-1, y)) + grid_traveler((x, y-1))
        return memo[key]


print(grid_traveler((0, 1)))
print(grid_traveler((1, 0)))

print(grid_traveler((1, 1)))
print(grid_traveler((1, 2)))
print(grid_traveler((2, 1)))
print(grid_traveler((2, 2)))

print(grid_traveler((2,3)))
print(grid_traveler((30,30)))
