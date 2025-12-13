def f(liczba):
    liczba_str = str(liczba)         
    suma = 0
    for cyfra in set(liczba_str):       
        ile_razy = liczba_str.count(cyfra)
        if ile_razy > 1:                
            suma += ile_razy * int(cyfra)
    return suma


print(f(1027))      
print(f(230335))    
print(f(51355307)) 
