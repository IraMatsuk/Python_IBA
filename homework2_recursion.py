len = int(input("Длина:  "))
h = int(input("Высота: "))


def cut_rectangle_on_squares(length, height):
    if length == 0 or height == 0:
        return 0
    min_side = min(length, height)
    max_side = max(length, height)
    print("Квадрат: " + str(min_side) + "x" + str(min_side))
    if length == height:
        return 1
    return cut_rectangle_on_squares(min_side, max_side - min_side) + 1


print("Количество квадратов: " + str(cut_rectangle_on_squares(len, h)))
