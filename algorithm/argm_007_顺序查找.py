import random

def linear_search(data, value):
    for index, item in enumerate(data):
        if item == value:
            return index
    return None

data = [random.randint(0, 100) for _ in range(10)]
print(data)
print(linear_search(data, 20))
