'''
第一个三引号注释
'''
# nonlocal: 在内函数中使用，可以使用上一层函数中的局部变量

# 在内函数中如何使用上一层函数中的局部变量

# 关于函数的文档

def outer():
    '''
    This is outer function
    :return: None
    '''
    num = 10
    def inner():
        nonlocal num
        num = 100
        print(num)
    inner()

outer()
print(__doc__)
print(outer.__doc__)