list1 = input ("Ввести строку из нескольких слов, разделенных пробелами")
list2 = list1.split()
for i, x in enumerate(list2, start=1):
    print (i )
    print (x [:10])
