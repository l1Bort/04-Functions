def f(kostki):
    max_count = 1
    current_count = 1
    max_digit = kostki[0]

    for i in range(1, len(kostki)):
        if kostki[i] == kostki[i - 1]:
            current_count += 1
            if current_count > max_count:
                max_count = current_count
                max_digit = kostki[i]
        else:
            current_count = 1

    return int(max_digit)

print(f("5233165554211"))  
print(f("2133"))          
