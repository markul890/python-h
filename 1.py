def my_num ():
    try:
        first = int(input(" vvedite pervoe chislo :"))
        second = int(input("vvedite vtoroe chislo :"))
    except ZeroDivisionError:
        return
    result = first // second
    return result
result = my_num()

print (result)
