def power(a, n): 
    if n == 0: 
        return 1 
    elif n % 2 == 1: 
        return power(a, n - 1) * a 
    else: 
        return power(a, n // 2)*power(a, n // 2) 
        
a = float(input("Будь ласка введіть числo a ")) #вводимо значення a, a > 0 
n = int(input("Будь ласка введіть числo n ")) #вводимо значення n, n > 0 	
print(power(a,n)) #викликаємо функцію та виводимо резульатат, що вона повертає         
