# 既然可以把函数作为一个参数传递，如果在一个函数中返回一个函数，那么这个被返回的函数就是一个闭包函数
# 在一个函数中的返回值是一个内函数，而且这个函数还使用了外函数的局部变量，这个内函数就是一个闭包函数

# 闭包的作用：
# 1. 闭包可以保护外部函数中的变量不被修改

# 检测一个函数是否为闭包函数：函数名.__closure__。如果是闭包函数，返回的是一个元组，元组中保存的是cell对象，cell对象中保存的是外部函数的局部变量

# money = 0
# def work():
#     global money
#     money += 100
#     return money

# def overtime():
#     global money
#     money += 200
#     return money

# def gouwu():
#     global money
#     money -= 50
#     return money

# work()
# work()
# work()
# overtime()
# gouwu()

# print(money)

def person():
    money = 0
    def work():
        nonlocal money
        money += 100
        print(money)
        return money
    
    def overtime():
        nonlocal money
        money += 200
        return money
    
    def buy():
        nonlocal money
        money -= 50
        return money
    
    return work

res = person()   # res = work
res()
res()
res1 = res()
res1 = res()
print(res1)
print(res.__closure__)