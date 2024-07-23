# 1. 关键字蚕食定义在“收集参数”后面
# 2。 关键字参数在实参中必须传递
def f1(a, b=2, *args, name):
    print(args)
    print(name)

f1(1, 2, 3, 4, 5, name='james')
f1(1,2, 3, 4, 5, 6)


