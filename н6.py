#a
from itertools import count

for el in count (10):
    if el > 20:
        break
    else:
        print(el)

#b
from itertools import cycle

c = 0
for el in cycle ("HAPPY"):
    if c > 20:
        break
    print (el)
    c+=1