import random
random.randint(1, 10)

print("Hello World")

import sys

# 查看当前使用的 Python 解释器路径
print("Python Interpreter Path:", sys.executable)

# 寻找质数
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
        return True
    
print(is_prime(7))

# 冒泡排序
