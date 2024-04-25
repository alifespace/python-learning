# 测试运行时间的装饰器
import time

def timeit(fn):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        fn(*args, **kwargs)
        t2 = time.time()
        print("Function %s cost %s seconds." % (fn.__name__, t2 - t1))
        return t2 - t1
    return wrapper

# 汉诺塔问题
@timeit
def Hanoi(n, A, B, C):
    if n > 0:
        Hanoi(n-1, A, C, B)
        print("Move a dish from %s to %s." % (A, C))
        Hanoi(n-1, B, A, C)

Hanoi(3, 'A', 'B', 'C')

# 乱序排列 0～9
import random
data = list(range(10))
random.shuffle(data)
print(data)

# 查找一个给定列表中某个值的索引
@timeit
def linear_search(data, value):
    for index, item in enumerate(data):
        if value == item:
            return index
    return None

print("index of data is: %s." % linear_search(data, 3))


# 二分法查找排序列表
def binary_search(data, value):
    left = 0
    right = len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == value:
            return mid
        elif mid < value:
            left = mid + 1
        else:
            right = mid - 1

    return None

data1 = list(range(10))
print("data1 is: %s." % data1)
print("Index of data1 is: %s." % binary_search(data1, 3))


