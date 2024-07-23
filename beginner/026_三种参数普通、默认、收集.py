# 至少要传递2个，最后1个参数是默认参数，需要在定义形参时，指定默认值
def f1(x, y, i=0):
    print(x, y, i)

f1(1, 2, 3)
f1(1, 2)

# 收集参数： 

def f2(*args):
    print(type(args))
    result = 0
    for i in args:
        result = result + i
    return result

print(f2(100, 200, 300))
