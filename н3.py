with open ("text_3hw.txt") as file:
    my_list = [my_line.split() for my_line in file.readlines()]

my_workers = [{"name": a[0], "money": int( a[1])}
     for a in my_list
     if len (a) > 1]

for a in my_workers:
    if a ["money"] < 20000:
        print(a["name"])

