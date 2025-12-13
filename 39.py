def sum_natural(n):
    if n == 1:
        return 1
    else:
        return n + sum_natural(n - 1)

n = 10
result = sum_natural(n)
print(f"The sum of natural numbers from 1 to {n} is: {result}")
