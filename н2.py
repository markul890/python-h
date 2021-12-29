first_list = [6, 9, 20, 1, 3, 90,15, 7, 87, 14]
second_list = [el for el in first_list if el > first_list[first_list.index (el)-1]]
print(second_list)

