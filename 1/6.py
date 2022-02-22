import sys


def build_matrix(data, lines, columns):
    if len(data) != lines * columns:
        print("Ты кого пытаешься обмануть???")
        sys.exit()

    matrix = []
    cut_counter = 0

    for i in range(1, lines + 1):
        line = data[cut_counter:columns * i]
        matrix.append(line)

        cut_counter += columns

    return matrix


def print_matrix(matrix):
    for line in matrix:
        print(*line)


def square_matrix(matrix, lines, columns):
    for i in range(lines):
        for j in range(columns):
            matrix[i][j] *= matrix[i][j]
    return matrix


def transp_matrix(matrix, lines, columns):
    tr_matrix = [[0 for j in range(lines)] for i in range(columns)]

    for i in range(lines):
        for j in range(columns):
            tr_matrix[j][i] = matrix[i][j]

    return tr_matrix


def minor(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]


def find_det(matrix):
    if len(matrix[0]) > 2:
        result = 0
        for i in range(len(matrix[0])):
            new_arr = []
            for j in range(len(matrix[0])):
                if j != i:
                    new_arr.append([matrix[j][k] for k in range(1, len(matrix[0]))])
            result += find_det(new_arr) * matrix[i][0] * (-1 + 2 * ((i + 1) % 2))
        return result
    else:
        return minor(matrix)


number_of_line = int(input("Ведите количество строчек матрицы \n"))
number_of_columns = int(input("Введите количество столбцов матрицы \n"))
elements = list(map(int, input("Через ЗАПЯТУЮ перечислите элементы матрицы \n").split(",")))

matrix = build_matrix(elements, number_of_line, number_of_columns)

print("Итак, вот ваша матрица: ")
print_matrix(matrix)
print(
    "Что вы желаете с ней сделать? (Введите цифру, соответствующую номеру операции с матрицей."
    " Для выхода из программы введите 0)\n",
    "1) Возвести в квадрат\n",
    "2) Транспонировать\n",
    "3) Найти определитель\n")

while True:
    command = input()

    if command == "1":
        new_matrix = square_matrix(matrix, number_of_line, number_of_columns)
        print_matrix(new_matrix)
    elif command == "2":
        new_matrix = transp_matrix(matrix, number_of_line, number_of_columns)
        print_matrix(new_matrix)
    elif command == "3":
        if number_of_columns != number_of_line:
            print("Сожалею, но определитель может быть вычислен только для квадратной матрицы ")
        else:
            det = find_det(matrix)
            print(det)
    elif command == "0":
        break
