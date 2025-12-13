def f(product_code):
    digits = [int(digit) for digit in product_code]
    sum_first_three = sum(digits[:3])
    return sum_first_three % 7 == digits[3]


print(f("1082")) 
print(f("2035")) 
print(f("1114")) 
print(f("7071")) 
