translation= {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
new = []

with open ("text_4.txt") as file:
    for i in file:
        i = i.split(" ", 1)
        new.append(translation[i[0]] + " " + i[1])

with open ("text_4new.txt", "w") as file_new:
    file_new.writelines(new)
