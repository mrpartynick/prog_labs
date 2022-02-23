numbers = list(map(int, input().split(",")))


def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def dwarf_sort(arr):
    i = 1
    n = len(arr)
    while i < n:
        if (arr[i - 1] <= arr[i]):
            i += 1
        else:
            tmp = arr[i]
            arr[i] = arr[i - 1]
            arr[i - 1] = tmp
            i -= 1
            if (i == 0):
                i = 1
    return arr


def block_sort(arr):
    def insertion_sort(arr):
        l = arr

        for i in range(0, len(l)):
            for j in range(i, 0, -1):
                if l[j] < l[j - 1]:
                    l[j], l[j - 1] = l[j - 1], l[j]
                else:
                    break
        return l

    max_value = max(arr)
    size = max_value / len(arr)

    # Создаем n пустых блоков, где n равно длине входного списка
    buckets_list = []
    for x in range(len(arr)):
        buckets_list.append([])

        # Помещаем элементы списка в разные блоки на основе size
    for i in range(len(arr)):
        j = int(arr[i] / size)
        if j != len(arr):
            buckets_list[j].append(arr[i])
        else:
            buckets_list[len(arr) - 1].append(arr[i])

    # Сортируем элементы внутри блоков с помощью сортировки вставкой
    for z in range(len(arr)):
        insertion_sort(buckets_list[z])

    # Объединяем блоки с отсортированными элементами в один список
    final_output = []
    for x in range(len(arr)):
        final_output = final_output + buckets_list[x]
    return final_output


def heapsort(alist):
    def parent(i):
        return (i - 1) // 2

    def left(i):
        return 2 * i + 1

    def right(i):
        return 2 * i + 2

    def max_heapify(alist, index, size):
        l = left(index)
        r = right(index)
        if (l < size and alist[l] > alist[index]):
            largest = l
        else:
            largest = index
        if (r < size and alist[r] > alist[largest]):
            largest = r
        if (largest != index):
            alist[largest], alist[index] = alist[index], alist[largest]
            max_heapify(alist, largest, size)

    def build_max_heap(alist):
        length = len(alist)
        start = parent(length - 1)
        while start >= 0:
            max_heapify(alist, index=start, size=length)
            start = start - 1

    build_max_heap(alist)
    for i in range(len(alist) - 1, 0, -1):
        alist[0], alist[i] = alist[i], alist[0]
        max_heapify(alist, index=0, size=i)

    return alist

print(bubble_sort(numbers),
      dwarf_sort(numbers),
      block_sort(numbers),
      heapsort(numbers))
