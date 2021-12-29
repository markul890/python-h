my_list_1 = [4, 4, 6, 12,12, 2, 99, 99, 6, 5,5, 11, 73, 73, 2,2]
print ( my_list_1)

my_list_2 = []
for el  in my_list_1 :
   if el not in my_list_2:
       my_list_2.append(el)
print (my_list_2)
