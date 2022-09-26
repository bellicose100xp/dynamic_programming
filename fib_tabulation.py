def fib(n: int) -> int:
    table: list[int] = [0]*(n+1)
    table[1] = 1  # base case
    for i in range(0, n):
        table[i+1] += table[i]
        if i < n - 1:
            table[i+2] += table[i]
    return table[n]


print(fib(5))
print(fib(6))
print(fib(7))
print(fib(8))
print(fib(50))
