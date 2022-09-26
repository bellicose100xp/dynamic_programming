from typing import cast
def how_sum(target: int, nums: list[int]) -> list[int] | None:
    table: list[list[int] | None] = [None]*(target + 1)

    # base case
    table[0] = []

    for i in range(0, target + 1):
        if table[i] is not None:
            for num in nums:
                if not i+num > len(table) - 1:
                    table[i+num] = [*cast(list[int], table[i]), num]
    
    return table[target]

print(how_sum(7, [2, 3]))
print(how_sum(7, [2, 4]))
print(how_sum(7, [5, 3, 4, 7]))
print(how_sum(8, [2, 3, 5]))
print(how_sum(300, [7, 14]))
