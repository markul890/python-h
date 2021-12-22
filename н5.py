value = int(input("введите число: "))
my_list = [5, 5, 4, 3, 3, 2, 2]
count = 0
for i in my_list:
    if value > i:
        rating.insert(count,a)
    if value == i:
        my_list.insert(count + my_list.count(i), value)
    count += 1

print (my_list)

# сидела над задачкой несколько ночей, но так до конца и не придумала...
