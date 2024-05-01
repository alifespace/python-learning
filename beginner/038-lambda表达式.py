'''
lambda 参数列表:返回值
'''

res = lambda x,y:x+y
print(res(4,5))

res = lambda sex:'Male' if sex=='M' else 'Female'
print(res('F'))