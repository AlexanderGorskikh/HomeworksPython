"""
Задача 6: Вы пользуетесь общественным транспортом?
Вероятно, вы расплачивались за проезд и получали билет с номером.
Счастливым билетом называют такой билет с шестизначным номером,
где сумма первых трех цифр равна сумме последних трех.
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
Вам требуется написать программу, которая проверяет счастливость билета.

*Пример:*

385916 -> yes
123456 -> no
"""

number = input('Enter your six-size number: ')

if len(number) != 6:
    print('Your number is not six-size')
else:
    right = 0
    left = 0

    for i in -1, -2, -3:
        right += int(number[i])

    for n in 1, 2, 3:
        left += int(number[i])

    if right != left:
        print('Your ticket is lucky')
    else:
        print('Your ticket is unlucky')
