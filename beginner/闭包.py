# 闭包
# 1. 需要存在嵌套函数
# 2. 嵌套函数需要引用外部函数的变量
# 3. 外部函数需要返回内部函数

def out_func(num):
    def inner_func(in_num):
        print(num)
        print(in_num, inner_func)
    return inner_func

result1 = out_func(10)
print(result1)
result1(5)

result2 = out_func(20)
print(result2)
result2(5)

# 装饰器: 不用修改被装饰的函数，但是可以给这个被装饰的函数添加功能
# 1.需要存在闭包
# 2. 需要存在被装饰的函数
# 3. 装饰器会将被装饰的函数当作参数传递给装饰器的同名函数

def welcome(func):
    def in_func():
        print("欢迎光临!")
        print("in_func address: %s." % in_func)
        func()
    return in_func

@welcome
def login():
    print("login address: %s is as same as in_func" % login)
    print("登陆成功！")

login()