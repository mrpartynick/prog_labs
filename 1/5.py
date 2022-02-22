import matplotlib.pyplot as plt
import gspread


def build_graph(x, y):
    plt.plot(x, y)
    plt.show()
    print("Введите через запятую x-координаты ")
    x_coords = list(map(int, input().split(",")))
    print("Введите через запятую у-координаты ")
    y_coords = list(map(int, input().split(",")))


def build_sheet(x_coordinates, y_coordinates):
    sa = gspread.service_account()
    sh = sa.open("Задача № 5")
    wks = sh.worksheet("Лист1")

    for i in range(0, 30):
        if i == 1:
            wks.update("A1", "X-coordinates")
            wks.update("B1", "Y-coordinates")
            continue
        updatable_x_cell = "A" + str(i + 2)
        updatable_y_cell = "B" + str(i + 2)
        wks.update(updatable_x_cell, str(x_coordinates[i]))
        wks.update(updatable_y_cell, str(y_coordinates[i]))


def least_square_method(x_coordinates, y_coordinates):
    x_middle = sum(x_coordinates)/len(x_coordinates)
    y_middle = sum(y_coordinates)/len(y_coordinates)

    print(x_middle)
    print(y_middle)

    x_deviation_from_middle = 0
    numerator = 0

    for i in range(len(x_coordinates)):
        x_deviation_from_middle = x_deviation_from_middle + (x_coordinates[i] - x_middle)
        numerator += (x_coordinates[i] - x_middle)*(y_coordinates[i] - y_middle)


    b1 = 0
    b2 = 0

    if x_deviation_from_middle != 0:
        b2 = numerator/(x_deviation_from_middle**2)
        b1 = y_middle - (b2*x_middle)
        return "Yi = " + str(b1) + "+" + str(b2) + "* Xi"
    else:
        return "Yi = Xi"


x_range = list(map(int, input("Через ЗАПЯТУЮ введите минимальную и максиальную х-координату ").split(",")))
y_range = list(map(int, input("Через ЗАПЯТУЮ введите минимальную и максиальную y-координату ").split(",")))

x_coordinates = [i for i in range(x_range[0], x_range[1])]
y_coordinates = [i for i in range(y_range[0], y_range[1])]

mnk = least_square_method(x_coordinates, y_coordinates)

build_sheet(x_coordinates, y_coordinates)
print(mnk)
build_graph(x_coordinates, y_coordinates)


