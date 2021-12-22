my_input = input("впишите элементы через запятую: ")
my_input = my_input.split(",")
for i in range(len(my_input)//2):
    my_input[2*i], my_input[2*i+1] = my_input[2*i+1], my_input[2*i]
print(my_input)