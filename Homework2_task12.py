# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

flag = True
while flag:
      Xmind = int(input())
      Ymind = int(input())
      if (Xmind > 0 and Xmind <= 1000 and Ymind > 0 and Ymind <= 1000):
            flag = False
      else: print('По условию задачи, числа не могут превышать 1000 или быть отрицательными')

x = 0
y = 0

while x != Xmind and x<1000:
      x+=1

while y != Ymind and y<1000:
      y+=1

print(f'Число x равно: {x}\n'
      f'Число y равно: {y}')











