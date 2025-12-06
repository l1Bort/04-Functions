import range_check

number = int(input("A number: "))
x = 2
y = 15

if range_check.in_range(number, x, y):
    result = "yes"
else:
    result = "no"

print(f"Number {number} in the range <{x},{y}>: {result}")
