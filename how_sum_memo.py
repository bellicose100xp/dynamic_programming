def how_sum(target_sum: int, nums: list[int], memo: dict[int, list[int] | None] | None = None) -> list[int] | None:

    if memo == None:
        memo = {}

    if target_sum in memo:
        return memo[target_sum]

    if target_sum < 0:
        return None

    if target_sum == 0:
        return []

    for num in nums:
        remainder = target_sum - num
        result = how_sum(remainder, nums, memo)

        if result is not None:
            memo[target_sum] = [*result, num]
            return memo[target_sum]

    memo[target_sum] = None
    return None

# Input, m = target_sum, n = array length
# Brute Force
# time: O(n^m * m) -> exponential time complexity
# space: O(m) -> linear space

# Optimized Solution
# time: O(m^n * n) -> polynomial time complexity
# space: O(m^2) -> polynomial space complexity

print(how_sum(5, [2, 3, 4]))
# print(how_sum(7, [2, 3]))
# print(how_sum(7, [2, 4]))
# print(how_sum(8, [2, 2, 5]))
# print(how_sum(300, [7, 14]))
