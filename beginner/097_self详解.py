# self是方法中的一个形参，并不是关键字，表示对象本身，类似于java中的this
# self指的是调用该方法的对象本身
# self访问对象的属性和方法


class Person:
    name = '名字'
    age = '年龄'
    sex = '性别'

    def sing(self):
        print('我会唱歌')
    
    def dance(self):
        print('我会跳舞')

    def rap(self):
        print('我会rap')

    def func(self):
        # 在类的内部访问对象的属性和方法
        print(self)
        print(self.name, self.age, self.sex)

    # 在类中定义的方法，如果没有self参数，这个方法不能使用对象去调用，这种方法只能用类名去调用，成为绑定类方法
    # 错误：def func2():


person1 = Person()
print(person1.name, person1.age, person1.sex)
person1.name = '张三'
print(person1)
person1.func()

