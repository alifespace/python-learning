from collections.abc import Iterator, Iterable

# iter() 将一个可迭代对象转化为迭代器对象

arr = ['apple', 'orange', 'grape', 'watermelon', 'lime', 'lemon', 'peach']
iter1 = iter(arr)
print(iter1, type(iter1))
res = next(iter1)
print(res)
res = next(iter1)
print(res)

iter1 = iter(arr)
for items in iter1:
    print(items)

# 检测迭代器对象
var1 = '123456'
iter1 = iter(var1)
print(isinstance(var1, Iterable))
print(isinstance(var1, Iterator))
print(isinstance(iter1, Iterator))