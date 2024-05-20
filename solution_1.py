# Задание 1

def find_element(lst, element):
    for item in lst:
        if item == element:
            return True
    return False
    
print(find_element([1, 2, 3, 4, 5], 6))
print(find_element(['a', 'b', 'c', 'd'], 'c'))
