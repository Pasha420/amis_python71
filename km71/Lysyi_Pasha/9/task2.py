def power(a, n): #визначаємо функцію
	result = 1 #вводимо змінну, в яку ми будемо записувати результат
	count = 1 #вводимо лічильник
	while(count <= n): #впроваджуємо цикл 
		result = result*a #збільшуємо наш результат на а 
		count = count + 1 #збільшуємо лічильник на 1 	 
	return result #повертаємо результат 
	
a = float(input("Будь ласка введіть числo a ")) #вводимо значення a, a > 0 
n = int(input("Будь ласка введіть числo n ")) #вводимо значення n	
print(power(a,n)) #викликаємо функцію та виводимо резульатат, що вона повертає 