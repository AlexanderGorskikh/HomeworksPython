# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
import re

# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские,
# либо только русские буквы.
#
# *Пример:*
#
# ноутбук
#     12

st = input("Введите текст: ")
st = st.upper()
print(st)
result = 0
# Заменяем латинские буквы на числа
st = re.sub("[AEIOULNSTR]", "1", st)
st = re.sub("[DG]", "2", st)
st = re.sub("[BCMP]", "3", st)
st = re.sub("[FHVWY]", "4", st)
st = re.sub("K", "5", st)
st = re.sub("[JX]", "8", st)
st = re.sub("[QZ]", "55", st)
# Заменяем кириллицу на числа
st = re.sub("[АВЕИНОРСТ]", "1", st)
st = re.sub("[ДКЛМПУ]", "2", st)
st = re.sub("[БГЁЬЯ]", "3", st)
st = re.sub("[ЙЫ]", "4", st)
st = re.sub("[ЖЗХЦЧ]", "5", st)
st = re.sub("[ШЭЮ]", "8", st)
st = re.sub("[ФЩЪ]", "55", st)
st = re.sub("\D", "", st)
print(st)
for i in range(0, len(st)):
        result+= int(st[i])

print(f"Ценность слова составляет: {result}")