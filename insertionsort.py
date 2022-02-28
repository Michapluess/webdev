from random import randint


list = []


for i in range(100):
    list.append(randint(1, 100))



#für 15es element  list[14]

for i in range(len(list)):
    x = list[i]
    j = i
    for j in range(j, 0, -1):
        y = list[j-1]
        if x < y:
            list[j-1] = x
            list[j] = y
        else:
            break


print(list)
