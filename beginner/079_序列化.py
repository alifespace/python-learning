# 内置模块：安装python解释器后自动安装，在需要时导入，不需要安装
# 序列化模块：一般数据在程序与网络中进行传输和存储时，需要以更加方便的方式进行传输和存储，因此需要对数据进行序列化
# pickle: 用于序列化和反序列化，将数据转换为二进制数据，存储在文件中，或者通过网络传输
# dumps()，序列化，可以把一个python任意对象序列化为一个二进制
# loads()，反序列化，可以把一个序列化后的二进制数据反序列化为python对象
# dump()，序列化，把一个数据对象进行序列化，并写入文件中
# load()，反序列化，读取一个文件中已经序列化的对象并反序列化

import json, pickle

class Person:
    name = None
    sex = None

    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def sing(self):
        print('唱歌')

p1 = Person('张三', '男')

with open('./test.json', 'wb') as f:
    pickle.dump(p1, f)

with open('./test.json', 'rb') as f:
    p2 = pickle.load(f)
    print(p2.name, p2.sex)
    p2.sing()

with open('./test.json', 'w') as f:
    json.dump(p1.__dict__, f)
    pass

with open('./test.json', 'r') as f:
    data = json.load(f)
    print(data)
    pass

vars1 = 'I love you!'
res = pickle.dumps(vars1)
print(res, type(res))

res = pickle.dumps(p1)
print(res, type(res))
