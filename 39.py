def sum_natural(n):
    # Przypadek bazowy: suma liczb do 1 to 1
    if n == 1:
        return 1
    # Rekurencyjnie obliczamy sumę dla n-1 i dodajemy n
    else:
        return n + sum_natural(n - 1)

# Obliczanie sumy liczb od 1 do 10
n = 10
result = sum_natural(n)
print(f"The sum of natural numbers from 1 to {n} is: {result}")
