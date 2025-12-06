def power(x, n):
    # Przypadek bazowy: x^0 = 1
    if n == 0:
        return 1
    # Rekurencyjnie obliczamy x^n = x * x^(n-1)
    else:
        return x * power(x, n - 1)

# Obliczanie 5^3
x = 5
n = 3
result = power(x, n)
print(f"The value of {x}^{n} is: {result}")
