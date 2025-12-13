def f(name):
    words = name.split()         
    acronym = ''                  

    for word in words:            
        first_letter = word[0]    
        acronym += first_letter.upper()  

    return acronym

print(f("Internet of Things"))  
print(f("For Your Information")) 
print(f("Python"))              
