"""
Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
Вместе они сделали S журавликов.
Сколько журавликов сделал каждый ребенок, если известно,
что Петя и Сережа сделали одинаковое количество журавликов,
а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

*Пример:*

6 -> 1  4  1
24 -> 4  16  4
    60 -> 10  40  10
"""

S = int(input('Enter summa cranes: '))

if S % 3 != 0:
    print('Из условия задачи следует, что число должно быть кратное 3-м')
else:
    Sergey_cranes = Peter_cranes = S / 6
    Katya_cranes = Peter_cranes * 4

    print(f'Peter made {Peter_cranes} cranes ')
    print(f'Sergey made {Sergey_cranes} cranes ')
    print(f'Katya made {Katya_cranes} cranes ')


