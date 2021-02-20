import math
import random

# task1
# 1. Ввести три числа m, n, p. Подсчитать количество отрицательных чисел.
m = int(input("Введите целое число:\n"))
n = int(input("Введите целое число:\n"))
p = int(input("Введите целое число:\n"))

count = 0
if m < 0:
    count += 1
if n < 0:
    count += 1
if p < 0:
    count += 1
print("Количество отрицательных чисел равно " + str(count))

# 2. Определить, имеется ли среди трёх чисел a, b и c хотя бы одна пара равных между собой чисел.

a = int(input("Введите целое число:\n"))
b = int(input("Введите целое число:\n"))
c = int(input("Введите целое число:\n"))

if a == b or a == c or b == c:
    print("Есть пара равных между собой чисел")
else:
    print("Равных между собой чисел нет")

# 3. Даны три числа a, b и c. Найти среднее геометрическое этих чисел, если все они отличны от нуля,
# и среднее арифметическое в противном случае.

a = int(input("Введите целое число:\n"))
b = int(input("Введите целое число:\n"))
c = int(input("Введите целое число:\n"))

if a and b and c != 0:
    geometric_mean = math.sqrt(a * b * c)
    print("Среднее геометрическое трёх чисел " + str(geometric_mean))

else:
    arithmetic_mean = (a + b + c) / 3
    print("Среднее арифметическое трёх чисел " + str(arithmetic_mean))


# 4. По номеру месяца напечатать пору года.

def seasons(month_number):
    if month_number == 1 or month_number == 2 or month_number == 12:
        return "This is winter time!"
    elif month_number == 3 or month_number == 4 or month_number == 5:
        return "This is spring time!"
    elif month_number == 6 or month_number == 7 or month_number == 8:
        return "This is summer time!"
    elif month_number == 9 or month_number == 10 or month_number == 11:
        return "This is autumn time"
    else:
        return "Wrong number of month"


print(seasons(12))
print(seasons(6))


# 5. Определить, есть ли среди заданных целых чисел A, B, C, D хотя бы одно нечётное.
def odd_number(a, b, c, d):
    if a < 0 or b < 0 or c < 0 or d < 0:
        return "Есть нечетное число"
    else:
        return "Все числа четные"


print(odd_number(1, -6, 10, 0))
print(odd_number(1, 6, 10, 0))


# 6. Дано натуральное трехзначное число n.
# Верно ли, что среди его цифр есть 0 или 9?

def natural_number(num):
    number = map(int, str(num))
    for i in number:
        if int(i) == 0 or int(i) == 9:
            return "Есть цифра " + str(i)


print(natural_number(450))
print(natural_number(492))

# 7. В переменную Y ввести номер года. Определить, является ли год високосным.
print("Введите год: ")
y = int(input())
if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
    print("Високосный год")
else:
    print("Не високосный год")


# 8. Дано натуральное четырехзначное число n. Верно ли, что все его цифры различны?

def are_numbers_different(number):
    num1 = int(number / 1000)
    num2 = int((number - num1 * 1000) / 100)
    num3 = int((number - num1 * 1000 - num2 * 100) / 10)
    num4 = number % 10
    if num1 != num2 and num2 != num3 and num3 != num4 and num4 != num1:
        return "Все числа различны"
    else:
        return "Не все числа различны"


print(are_numbers_different(1234))
print(are_numbers_different(1124))


# 9. Проверить, является ли дробь A / B правильной.

a = int(input("Введите целое число:\n"))
b = int(input("Введите целое число:\n"))

if a > b:
    print("Дробь правильная")
else:
    print("Дробь неправильная")


# task2
# 2. Торговая фирма в первый день работы реализовала товаров на P тыс. руб., а затем ежедневно увеличивала
# выручку на 3%. # Какой будет выручка фирмы в тот день, когда она впервые превысит заданное значение Q? # Сколько

p = float(input("Введите прибыль в первый день: "))
q = float(input("Введите заданное значение: "))
count_days = 0

while p < q:
    p = p + p * 0.03
    count_days += 1
print("Сколько дней придется торговать фирме для достижения этого результата: " + str(count_days))
print("Выручка фирмы в тот день, когда она впервые превысит заданное значение q: " + str(p))


# task3
n = int(input("Введите размер списка:\n"))
A = []  # создание пустого списка

for i in range(n):
    a = random.randint(0, 99)  # генерация случайного числа
    A.append(a)  # добавление числа в список
print("Список рандомных чисел:\n" + str(A))

"""
# 1. Удалить элемент с введенным номером a.
a = int(input("Введите номером элемента для удаления:\n"))
A.remove(a)
print("Список после удаления элемента:\n" + str(A))
"""

# 2. Все четные по значению элементы исходного списка A поместить в новый список B.
B = []
for i in A:
    if i % 2 == 0:
        B.append(i)
print("Список В c четными значениями элементов из списка А:\n" + str(B))
"""
# 3. Удалить элементы, индексы которых кратны 7.
for i in reversed(range(7, len(A), 7)):
    A.pop(i)
print("Список после удаления элементов, индексы которых кратны 7:\n" + str(A))
"""

# 4 Найти значение минимального элемента списка.
print("Значение минимального элемента списка:\n" + str(min(A)))

"""
#  6.Удалить все элементы с заданным значением, если они имеются в списке.
remove_elem = int(input("Введите значение для удаления элементов:\n"))
for i in A:
    if i == remove_elem:
        A.remove(i)

print("Список после удаления элемента:\n" + str(A))
"""

"""
# 7. Удалить из списка все элементы, совпадающие с его минимальным значением.
min_elem = min(A)
for i in A:
    if i == min_elem:
        A.remove(i)
print("Список после удаления элементов с минимальным значением:\n" + str(A))
"""

# 8. Найти значение максимального элемента списка.
max_elem = max(A)
print("Максимального значение элемента списка: \n" + str(max_elem))

# 9. Найти среднее арифметическое элементов списка.
arithmetic_mean = sum(A) / n
print("Среднее арифметическое элементов списка:\n" + str(arithmetic_mean))

# 10. Найти среднее арифметическое трех последних элементов списка.
for i in A:
    last_three_elem = A[-3:]
    arithmetic_mean = sum(last_three_elem) / 3
print("Среднее арифметическое трех последних элементов списка:\n" + str(arithmetic_mean))

"""
# 11. Удалить пять первых нечетных по значению элементов списка.
count_removed = 0
index = 0
while index < len(A):
    if A[index] % 2 != 0:
        A.pop(index)
        count_removed += 1
    else:
        index += 1
    if count_removed == 5:
        break

print("Список после удаления пяти первых нечетных по значению элементов:\n" + str(A))
"""

# 12. Найти номер минимального элемента списка.
for index in range(len(A)):
    if A[index] == min(A):
        print("Номер минимального элемента списка: " + str(index))

