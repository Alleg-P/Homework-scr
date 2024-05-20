# Задание 4

def sort_objects(lst, key):
    return sorted(lst, key=lambda x: x[key])

objects = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 20}, {'name': 'Charlie', 'age': 30}]
sorted_objects = sort_objects(objects, 'age')
print(sorted_objects)
