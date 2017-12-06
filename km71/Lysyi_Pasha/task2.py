def Min(list):#оголошення функції
    if len(list) == 1:
        return list[0]
    else:
        return min(Min(list[:-1]), list[-1]) #знаходження мінімального елменту за допомогою рекурсії 

print(Min(input("please write a list ").split())) #введення ліста та їх сплітування і визивання функції від ліста