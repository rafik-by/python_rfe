def unique_elements(nested_list, unique_list=None):
    if unique_list is None:
        unique_list = []

    for item in nested_list:
        if isinstance(item, list):
            unique_elements(item, unique_list)
        else:
            if item not in unique_list:
                unique_list.append(item)

    return unique_list


list_a = [1, 2, 3, [4, 3, 1], 5, [6, [7, [10], 8, [9, 2, 3]]]]

print(f"Исходный вложенный список: {list_a}")
result_unique = unique_elements(list_a)
print(f"Список уникальных элементов (с сохранением порядка обхода): {result_unique}")