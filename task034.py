# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто,
# насколько легко он их придумывает, Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов,
# то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами.
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке
# и “Пам парам”, если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
#     **Вывод:** Парам пам-пам


# input_single = str(input("Привет, Винни-Пух! Запиши свое стихотворение: "))

input_single = 'пара-ра-рам рам-пам-папам па-ра-па-да-ду'
print(input_single)
single_in_count = input_single.split()
print(single_in_count)

list_vowel = ['а', 'о', 'у', 'э', 'е', 'ё', 'и', 'ю', 'я']

count = []
for i in single_in_count:
    sum = 0
    for letter in i:
        if letter in list_vowel:
            sum += 1
    count.append(sum)
print(count)


if len(set(count)) == 1:
    print("Парам пам-пам")
else:
    print("Пам парам")


# count.append([[letter for letter in i if letter in list_vowel] for i in single_in_count])
#result = list(filter(lambda x: x[0] == x[i]  in range(len(count))))
# print(count)
# count = list(count)
# print(list(filter(lambda x: x[0] == x[1], count)))