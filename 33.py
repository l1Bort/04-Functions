def f(expression):
    expression = expression.replace('-', '+-') 
    parts = expression.split('+')
    
    total = 0
    for part in parts:
        if part:
            total += int(part)

    return total


print(f("2+3"))       
print(f("3+8+1"))    
print(f("2+3-4+5-0")) 
