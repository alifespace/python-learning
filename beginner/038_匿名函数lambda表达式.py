'''
lambda 参数列表:返回值
'''

# 匿名函数：不需要def定义，函数也不需要有名字，python可以使用lambda创建匿名函数，lambda函数的主体是一个表达式，而不是一个代码块，仅仅能在lambda表达式中封装有限的逻辑进去
# lambda只能访问自己的形参，不能访问自己的外部变量，包括全局变量和局部变量
# lambda条件表达式：lambda x: 'True' if x>10 else 'False'

res = lambda x,y:x+y
print(res(4,5))

res = lambda sex:'Male' if sex=='M' else 'Female'
print(res('F'))