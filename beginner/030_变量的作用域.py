# 变量的作用域：变量的有效范围
# 1. 局部变量
# 2. 全局变量：函数内外都可以使用的变量
#    - 对于函数外定义的全局变量，只能访问不能更新。可以在函数内使用global来引用函数外定义的全局变量

# 变量分两种：1. 可变数据类型；2. 不可变数据类型；
# 1. 可变数据类型：函数外定义的变量，函数内可以更新。包括列表和字典
# 2. 不可变数据类型：函数外定义的变量，函数内可以访问，不可更新

# 在函数内部使用 global 定义的变量是全局变量，可以函数内外访问和更改
# 在函数外定义的变量，在函数内使用global定义后，可以在函数内部更改

# 不光变量有作用域，函数也有作用域

lst1 = [1, 2, 3]
num = 10
num1 = 20
def f1():
    print(num)
    global num1  # num1 = 20, 可以直接修改全局变量
    # num = 20, 不可以直接修改全局变量

    lst1[2] = 4
    print(num1)
    num1 = 200
    lnum1 = 10
    print(lnum1)
    print(globals())
    print('locals()', locals())

f1()
print(num)
print(lst1)
print(num1)


# locals(): 获取当前作用域的数据
print("globals():", globals())  # 获取全局作用域的数据
print(locals())

def outer():
    var1 = '12'
    print('This is outer function')
    print(globals())
    print(locals())
    # inner 是一个局部函数，函数外无法直接使用
    def inner():
        print('This is inner function')

    inner()


outer()