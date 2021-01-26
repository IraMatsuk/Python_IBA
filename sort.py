import random

mas = [3, 5, 67, -65, 34, 21]
maximum = mas[1]
for i in range(1, len(mas)-1):
    if mas[i] > mas[i+1]:
        maximum = mas[i]
        print (maximum)

mas = [random.randint(0, 100) for i in range(20)]
print(mas)
for i in range(1, len(mas) - 1):
    if mas[i - 1] < mas[i] > mas[i + 1]:
        print(i, end=" ")

