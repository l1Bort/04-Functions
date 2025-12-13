def f(amount_to_pay):
    coins = [5, 2, 1]
    count = 0
    for coin in coins:
        count += (amount_to_pay // coin)
        amount_to_pay %= coin
    return count

print(f(23))  
print(f(8))  
print(f(2))   
print(f(0))   
