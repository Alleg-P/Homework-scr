# Задание 2

def binary_find_element(lst, element):
    left = 0
    right = len(lst) - 1

    while left <= right:
        middle = (left + right) // 2

        if lst[middle] == element:
            return True
        elif lst[middle] < element:
            left = middle + 1
        else:
            right = middle - 1

    return False

lst1 = []
element1 = 5
print(binary_find_element(lst1, element1))

lst2 = [1, 3, 5, 7, 9, 11]
element2 = 5
print(binary_find_element(lst2, element2))

lst3 = [2, 4, 6, 8, 10, 12, 14]
element3 = 6
print(binary_find_element(lst3, element3))
