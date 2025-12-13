def check(binary_number):
    for c in binary_number:
        if c != '0' and c != '1':
            return False
    return True

binary_number = "101101"
print(check(binary_number))  # True

binary_number = "1311a10100"
print(check(binary_number))  # False
