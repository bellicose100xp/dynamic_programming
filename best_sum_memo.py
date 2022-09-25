def best_sum_fn(target_sum: int, nums: list[int], memo: dict[int, list[int] | None] | None = None) -> list[int] | None:

    if memo == None:
        memo = {}
    
    if target_sum in memo:
        return memo[target_sum]

    best_sum: list[int] | None = None

    if target_sum < 0:
        return None

    if target_sum == 0:
        return []

    for num in nums:
        remainder = target_sum - num
        result = best_sum_fn(remainder, nums, memo)

        if result is not None:
            new_sum: list[int] = [*result, num]

            if best_sum is None or len(best_sum) > len(new_sum):
                best_sum = new_sum
    
    memo[target_sum] = best_sum
    return best_sum

print(best_sum_fn(7, [5, 3, 4, 7]))  # [7]
print(best_sum_fn(8, [2, 3, 5]))  # [3, 5]
print(best_sum_fn(8, [1, 4, 5]))  # [4, 4]
print(best_sum_fn(100, [1, 2, 5, 25]))  # [25, 25, 25, 25]
