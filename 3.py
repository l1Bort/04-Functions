###
# Calculates the sum of the digits in a number
#
def sum_digits(number):
    number = abs(number)
    sum_digits = 0
    while number > 0:
        number_str = str(number)
        last_digit_str = number_str[-1]
        last_digit = int(last_digit_str)    
        sum_digits += last_digit
        number = number // 10
    return sum_digits

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')