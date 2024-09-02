# 创建对象的时候，并不会复制父类的属性和方法，而是通过引用来访问父类的属性和方法
# 因此在访问对象的时候，会先访问对象的属性和方法，如果对象没有该属性和方法，再访问类的属性和方法
# 如果对象的属性和方法和类的属性和方法同名，会优先访问对象的属性和方法
# 访问成员属性：先访问对象的属性，如果对象没有该属性，再访问类的属性
class Cart:
    color = 'red'
    brand = 'BMW'

    def run(self):
        print('Cart is running')

    def stop(self):
        print('Cart is stopping')


car1 = Cart()
print(car1.color, type(car1), car1)
car1.run()

car2 = Cart()
print(car1, car2)
print(car2.color)
car2.color = 'green'
print(car2.color)

# python是动态语言，可以在类外部给对象添加属性
car2.abc = '123'   # abc是car2对象的属性, car1对象没有abc属性
print(car2.abc)

del car2.abc  # 只能删除对象的属性，不能删除类的属性
print(car2.color)  # green
del car2.color   # 删除的是对象的属性，不是类的属性
print(car2.color)  # red: 类的属性

# 访问对象的方法，如果对象没有该方法，再访问类的方法
# 修改对象的方法
def func1():
    print('func1')

car2.run()
car2.run = func1
car2.run()
del car2.run
car2.run() 

# 给对象添加方法
def func2():
    print('func2')

car2.test = func2
car2.test()