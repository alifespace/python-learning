# 内置模块：安装python解释器后自动安装，在需要时导入，不需要安装
# 序列化模块：
# pickle: 用于序列化和反序列化，将数据转换为二进制数据，存储在文件中，或者通过网络传输

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
