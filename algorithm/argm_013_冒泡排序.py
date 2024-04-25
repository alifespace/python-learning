import random, mytools

@mytools.timeit
def bubble_soft(data):
    for i in range(len(data) - 1):
        for j in range(len(data) - i - 1):
            if (data[j] > data[j+1]):
                data[j], data[j+1] = data[j+1], data[j]
    return data

data1 = list(range(20000))
random.shuffle(data1)
bubble_soft(data1)

data2 = [random.randint(0,10000) for i in range(10)]
print(data2)
bubble_soft(data2)
print(data2)
# print(data1)
