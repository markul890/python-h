time = int(input("ввести: "))
h = time // 3600
m = (time - h * 3600) // 60
s = time % 60
print (h, ":", m , ":", s)
