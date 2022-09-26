def can_sum(target: int, nums: list[int]) -> bool:
    table = [False]*(target + 1)

    # base case
    table[0] = True

    for i in range(0, target + 1):
        if table[i] == True:
            for num in nums:
                if not i+num > len(table) - 1:
                    table[i+num] = True
    
    return table[target]

print(can_sum(7, [2, 3]))
print(can_sum(7, [2, 4]))
print(can_sum(7, [5, 3, 4, 7]))
print(can_sum(8, [2, 3, 5]))
print(can_sum(300, [7, 14]))
