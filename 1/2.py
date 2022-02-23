from math import sqrt

input_data = input().split(",")


def sort_numbers(input_data):
    def is_prime(n):
        d = 2
        while d * d <= n and n % d != 0:
            d += 1
        return d * d > n

    def extract_real(n):
        is_number = False
        number = ""
        if n[0] == "s":
            for elem in n:
                if elem == ")":
                    is_number = False
                if is_number:
                    number += elem
                if elem == "(":
                    is_number = True

            number = int(number)

            return number
        return n

    natural = []
    integer = []
    rational = []
    real = []
    compl = []
    even = []
    not_even = []
    simple = []

    for elem in input_data:
        if elem[-1] == "i":
            compl.append(elem)
            continue
        else:
            if "s" in elem:
                elem = extract_real(elem)
                if str(sqrt(elem))[-1] != "0":
                    real.append("sqrt(" + str(elem) + ")")
                    continue
                else:
                    elem = str(sqrt(elem))[:-2]
            if "." in elem:
                if elem[elem.index(".") + 1] != "0":
                    rational.append(elem)
                    continue
                else:
                    elem = int(float(elem))
            else:
                elem = int(elem)

            if elem % 2 == 0:
                even.append(elem)
            else:
                not_even.append(elem)

            if is_prime(elem):
                simple.append(elem)

            if type(elem) == float:
                rational.append(elem)
            elif elem <= 0:
                integer.append(elem)
            elif elem > 0:
                natural.append(elem)

    print("Натуральные: ", *natural, "\n",
          "Целые: ", *integer, "\n",
          "Рациональные: ", *rational, "\n",
          "Иррациональные: ", *real, "\n",
          "Комплексные: ", *compl, "\n",
          "Чётные: ", *even, "\n",
          "Нечётные: ", *not_even, "\n",
          "Простые: ", *simple, "\n")


sort_numbers(input_data)
