"""
Задача 2: Найдите сумму цифр трехзначного числа.
*Пример:*

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) /
"""
number = input('Enter your number: ')
i = 0
result = 0

while (len(number) != i) :
    result += int(number[i])
    i += 1

print(f'Summa is : {result}')