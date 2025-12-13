def f(n):
    primes = []      
    num = 2          

    while len(primes) < n:
        is_prime = True   

        for p in primes:  
            if num % p == 0:
                is_prime = False
                break     

        if is_prime:
            primes.append(num)

        num += 1

    return primes[-1]

print(f(1)) 
print(f(5)) 
