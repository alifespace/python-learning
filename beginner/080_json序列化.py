# json在js中是一个对象的表示的方法，和python中的字典的定义规则和语法都很像
# json在互联网中是一种通用的数据定义、传输和交换的数据格式

import json

vardict1 = {'name':'admin', 'age': 20, 'sex': 'M'}
print(vardict1, type(vardict1))

res = json.dumps(vardict1)
print(res, type(res))

res = json.loads(res)
print(res, type(res))
print('Hello World!')

# 闭包
print('闭包')

# 序列化