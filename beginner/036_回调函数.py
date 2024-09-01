# 函数中的参数可以是任意类型的，包括函数本身

# 回调函数：函数的参数是一个函数，并且在函数中使用了传递进来的函数，这个传递进来的函数就是回调函数

def func1(f):
    print(f, type(f))
    f()

def func2():
    print('123')

func1(func2)