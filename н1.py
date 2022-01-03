lines = (input("строка1: "), input("строка2: "), input("строка3: "))
with open("f_1.txt", "w") as file:
    for line in lines:
        file.writelines(line+'\n')
