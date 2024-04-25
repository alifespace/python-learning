import random, mytools

@mytools.timeit
def select_soft_simple(data):
    data_new = []
    for i in range(len(data)):
        min_val = min(data)
        data_new.append(min_val)
        data.remove(min_val)

    return data_new

@mytools.timeit
def select_soft(data):
    for i in range(len(data) - 1):
        for j in range((i+1), len(data)):
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]
    return data

data1 = list(range(10000))
random.shuffle(data1)
data1 = select_soft(data1)
# data1 = select_soft_simple(data1)
# print(data1)