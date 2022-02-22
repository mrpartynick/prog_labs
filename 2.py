from math import sqrt

input_data = input().split(",")


def sort_numbers(input_data):
    def is_prime(n):
        d = 2
        while d * d <= n and n % d != 0:
            d += 1
        return d * d > n


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
            if "." in elem:
                elem = float(elem)
            else:
                elem = int(elem)

            real.append(elem)

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

    print(natural,integer,rational,real,compl,even,not_even,simple)


sort_numbers(input_data)
