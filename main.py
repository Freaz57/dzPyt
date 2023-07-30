# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12


# from random import randint

# n = int(input("Введите 1-ое число: "))
# list1 = [randint(0, 20) for i in range(n)]
# m = int(input("Введите 2-оe число: "))
# list2 = [randint(0, 20) for j in range(m)]
# print(f"Список 1 : {list1}")
# print(f"Список 2 : {list2}")
# list_1 = list(set(list1))
# list_2 = list(set(list2))
# print(f"Уникальный список 1 : {list_1}")
# print(f"Уникальный список 2 : {list_2}")
# list_uniq = []
# list_uniq = list(set(list_1) & set(list_2))
# list_uniq = sorted(list_uniq)
# print(f"Список с одинаковыми числами: {list_uniq}")


# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.
# 4 -> 1 2 3 4
# 9

from random import randint

n = int(input("введите кол-во кустов: "))
list1 = list(randint(1, 4) for i in range(n))  # узнаём сколько ягод на каждом кусте
print(list1)
a = int(input("введите номер куста: "))
res = 0
if a == 1:  # считаем для первого куста
    res = list1[0] + list1[1] + list1[-1]
elif a == (len(list1)):  # для последнего куста
    res = list1[-2] + list1[-1] + list1[0]
else:  # для остальных кустов
    res = list1[a - 1] + list1[a - 2] + list1[a]
print(f"столько ягод получится если модуль стоит перед {a} кустом: -> {res} <-")
