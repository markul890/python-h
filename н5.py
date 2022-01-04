
with open("text_5.txt", "w") as file:
    s = 0
    while True:
        n = int(input("введите числа, разделенные пробелами  "))
        s+=n
        print(s)
        file.writelines(my_str)

# сидела над ней несколько дней, очень сложно пока решить (