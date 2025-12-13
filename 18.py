def f(number, even):
    total = 0
    for digit in str(number):
        value = int(digit)
        if even:
            if value % 2 == 0:
                total += value
        else:
            if value % 2 != 0:
                total += value
    return total

print(f(3124, True))  
print(f(3124, False)) 
print(f(20576, False)) 
print(f(20576, True))  
print(f(13115, True)) 
