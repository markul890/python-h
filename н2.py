with open ("text.txt", "r") as file:
    content = file.readlines()
    print(f'количество строк - {len(content)}')

with open ("text.txt","r") as file:
    content = file.readline()
    content = content.split()
    print(f'количество слов в 1 строке - {len(content)}')
    content = file.readline()
    content = content.split()
    print(f'количество слов в 2 строке - {len(content)}')
    content = file.readline()
    content = content.split()
    print(f'количество слов в 3 строке - {len(content)}')