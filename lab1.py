import math

# task1
# Ввести три числа m, n, p. Подсчитать количество отрицательных чисел.
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

# task2
# Определить, имеется ли среди трёх чисел a, b и c хотя бы одна пара равных между собой чисел.

a = int(input("Введите целое число:\n"))
b = int(input("Введите целое число:\n"))
c = int(input("Введите целое число:\n"))

if a == b or a == c or b == c:
    print("Есть пара равных между собой чисел")
else:
    print("Равных между собой чисел нет")

# task3
# Даны три числа a, b и c. Найти среднее геометрическое этих чисел, если все они отличны от нуля,
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


# task4
# По номеру месяца напечатать пору года.

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


# task5
# Определить, есть ли среди заданных целых чисел A, B, C, D хотя бы одно нечётное.
def odd_number(a, b, c, d):
    if a < 0 or b < 0 or c < 0 or d < 0:
        return "Есть нечетное число"
    else:
        return "Все числа четные"


print(odd_number(1, -6, 10, 0))
print(odd_number(1, 6, 10, 0))


# task6
# Дано натуральное трехзначное число n.
# Верно ли, что среди его цифр есть 0 или 9?

def natural_number(num):
    number = map(int, str(num))
    for i in number:
        if int(i) == 0 or int(i) == 9:
            return "Есть цифра " + str(i)


print(natural_number(450))
print(natural_number(492))

# task7
# В переменную Y ввести номер года. Определить, является ли год високосным.
print("Введите год: ")
y = int(input())
if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
    print("Високосный год")
else:
    print("Не високосный год")


# task8
# Дано натуральное четырехзначное число n. Верно ли, что все его цифры различны?

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

# task9
# Проверить, является ли дробь A / B правильной.

a = int(input("Введите целое число:\n"))
b = int(input("Введите целое число:\n"))

if a > b:
    print("Дробь правильная")
else:
    print("Дробь неправильная")
