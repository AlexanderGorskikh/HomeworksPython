import re
# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто,
# насколько легко он их придумывает, Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв)
# в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова,
# если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”,
#  если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
#
# *Пример:*
#
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
#     **Вывод:** Парам пам-пам

song = 'пара-ра-рам рам-пам-папам па-ра-па-да'.lower()

text = song.split()
count_wowel = len(re.findall(r'[аоуыэеёиюя]', text[0]))
tmp = 0
res = True
for i in range(0, len(text)):
    tmp = len(re.findall(r'[аоуыэеёиюя]', text[i]))
    if count_wowel != tmp:
        res = False

result ='Парам пам-пам' if res else 'Пам парам'
print(result)