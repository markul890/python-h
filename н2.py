with open ("text_2hw.txt", "r") as f:
    content = f.readlines()
    print(f'Количество строк в файле - {len(content)}')

with open ("text_2hw.txt", "r") as f:
    a = str(f.readlines())
    print(len(set(a.split())))
