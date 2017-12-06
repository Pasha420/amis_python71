def backward(list):#оголошення функції
    if len(list) < 2:
        return list
    else:
        x = len(list)//2
        return backward(list[x:])+backward(list[:x]) #використання рекурсії для обернення ліста


print(backward(input("please write a list ").split())) ##введення ліста та їх сплітування і визивання функції від ліста
