profit = int (input ("введите значение выручки: "))
loss = int  (input ("введите значение издержки: "))
rent = profit / loss

if profit > loss:
    print ("выручка больше")
    print (rent)

if profit < loss:
    print("издержки больше")

workers = int (input ("введите число сотрудников:  "))
profit1 = profit / workers
print (profit1)
