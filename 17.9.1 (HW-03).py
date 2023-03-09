spisok = input("Введите последовательность чисел через пробел: ")
spisok_list = [int(a) for a in spisok.split()]
num = int(input("Введите любое число: "))
if num % 1 == 0:
        spisok_list.append(num)
        print("Список до сортировки: ", spisok_list)
def my_sort(spisok_list):
    for i in range(len(spisok_list)):  # проходим по всему массиву
        idx_min = i  # сохраняем индекс предположительно минимального элемента
        for j in range(i, len(spisok_list)):
            if spisok_list[j] < spisok_list[idx_min]:
                idx_min = j
        if i != idx_min:  # если индекс не совпадает с минимальным, меняем
            spisok_list[i], spisok_list[idx_min] = spisok_list[idx_min], spisok_list[i]
    return spisok_list

print("Список после сортировки:", my_sort(spisok_list))
def bi_search(a: int, spisok: list) -> int:
    left, right = 0, len(spisok)
    while left < right:
        middle = (left + right) // 2
        if spisok[middle] < a:
            left = middle + 1
        else:
            right = middle
    return left

print("Индекс введенного числа:", bi_search(num, spisok_list))

spisok_list.index(num, spisok_list.index(num) - 1, spisok_list.index(num) + 1)
print("Индекс соседник чисел:", spisok_list.index(num) - 1, spisok_list.index(num) +1)
