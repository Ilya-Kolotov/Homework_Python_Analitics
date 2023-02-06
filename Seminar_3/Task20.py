# Задача 20
# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
# Пример:
# Ввод:
# ноутбук
# Вывод:
# 12

alphabet_rus = {}
list_1 = 'А, В, Е, И, Н, О, Р, С, Т'
list_1 = list_1.split(', ')
for i in list_1:
    alphabet_rus.setdefault(i, 1)
list_1 = 'Д, К, Л, М, П, У'
list_1 = list_1.split(', ')
for i in list_1:
    alphabet_rus.setdefault(i, 2)
list_1 = 'Б, Г, Ё, Ь, Я'
list_1 = list_1.split(', ')
for i in list_1:
    alphabet_rus.setdefault(i, 3)
list_1 = 'Й, Ы'
list_1 = list_1.split(', ')
for i in list_1:
    alphabet_rus.setdefault(i, 4)
list_1 = 'Ж, З, Х, Ц, Ч'
list_1 = list_1.split(', ')
for i in list_1:
    alphabet_rus.setdefault(i, 5)
list_1 = 'Ш, Э, Ю'
list_1 = list_1.split(', ')
for i in list_1:
    alphabet_rus.setdefault(i, 8)
list_1 = 'Ф, Щ, Ъ'
list_1 = list_1.split(', ')
for i in list_1:
    alphabet_rus.setdefault(i, 10)

word = input("Введите слово - ")
word1 = word.upper()
sum = 0
for i in word1:
    for k, v in alphabet_rus.items():
        if i == k:
            sum += v
print(f'Стоимость введенного слова {word} = {sum}')