def f(number):
    num_str = str(number)
    repeated_sum = 0
    for digit in set(num_str):
        if num_str.count(digit) > 1:
            repeated_sum += int(digit) * (num_str.count(digit) - 1)
    return repeated_sum
