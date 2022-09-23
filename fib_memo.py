def fib(n: int, memo: dict[int, int] = {}) -> int:
    if n <= 2:
        return 1

    if n in memo.keys():
        return memo[n]
    else:
        memo[n] = fib(n-1) + fib(n-2)
        return memo[n]


print('fib(2): ', fib(2))
print('fib(4): ', fib(4))
print('fib(18): ', fib(300))
