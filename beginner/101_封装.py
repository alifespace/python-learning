# 面向对象的三个特性：封装、继承、多态
# 封装：将数据和行为封装到类中，对外部隐藏内部实现细节
# 封装的特点： 封装的成员一般供内部使用
# 封装的级别： 公有的、私有的(__)、受保护的(_)
# 在类的外部无法访问私有的成员，但是可以通过特殊的方式访问

class Person:
    # 公有的成员
    name = None
    __age = None
    _sex = None

    def __init__(self, name, age, sex) -> None:
        self.name = name
        self.__age = age
        self._sex = sex
        
    def say(self):
        print('My name is %s, I am %d years old.' % (self.name, self.age))

    def sing(self):
        print('I am singing.')

    def kiss(self):
        print('I am kissing you.')

person1 = Person('张三', 20, '男')

# 查看对象相关的成员
print(person1.__dict__)
print(Person.__dict__)
print(person1.__dir__())    # 查看对象的所有方法和属性

print(person1._sex)
# print(person1.__age)
person1._sex = '女'
print(person1._sex)