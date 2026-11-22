def flatten_list(lst):
    i = 0
    while i< len(lst): 
        if isinstance(lst[i], list):
            flatten_list(lst[i])
            lst[i:i+1] = lst[i]
        else:
            i += 1 


list_a = [1,2,3,4,[4],5,[6,[7,[],8,[9]]]]

# list_a =[list(map(int, input("Введите через пробел член списка: ").split())) 
#          for _ in range(int(input("Введите количество чисел в исходном списке: ")))]

flatten_list(list_a)

print(list_a)
