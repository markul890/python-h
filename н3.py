number = int(input ("number of month"))
my_list = ["winter", "spring", "summer", "autumn"]
my_dict = {1: "winter", 2: "spring", 3: "summer", 4: "autumn"}

if number == 1 or number == 12 or number == 2:
    print(my_list [0])
    print(my_dict.get (1))

if number == 3 or number == 4 or number == 5:
    print(my_list [1])
    print(my_dict.get (2))

if number == 6 or number == 7 or number == 8:
    print(my_list [2])
    print(my_dict.get (3))

if number == 9 or number == 10 or number == 11:
    print(my_list [3])
    print(my_dict.get (4))
