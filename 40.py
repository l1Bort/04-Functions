def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)

x = 5
n = 3
result = power(x, n)
print(f"The value of {x}^{n} is: {result}")
