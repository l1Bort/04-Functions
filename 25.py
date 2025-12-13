def f(n):
    a = 0
    b = 1
    for i in range(n - 1):
        c = a + b
        a = b
        b = c
    return a
# fibonacci

print(f(5))  
print(f(9))  
