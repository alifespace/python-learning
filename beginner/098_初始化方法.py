# 魔术方法：是不需要手动调用的方法，会在特定的时机自动调用
# 默认前后都有两个下划线，魔术方法无需我们定义，python会自动调用

# __init__：初始化方法，创建对象时自动调用，类实例化之后自动调用

class Person:
    name = None
    age = None
    sex = None

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def say(self):
        print('我会说话')


person1 = Person('张三', 18, '男')
print(person1.name, person1.age, person1.sex)