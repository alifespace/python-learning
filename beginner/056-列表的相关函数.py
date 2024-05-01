# len()
varlist1 = ['apple', 'orange', 'peach', 'watermelon', 'grape', 'banana', 'lime', 'lemon', 'Tangelo']
print(len(varlist1))

# count()
varlist1 = ['apple', 'orange', 'grape', 'peach', 'watermelon', 'grape', 'banana', 'lime', 'lemon', 'Tangelo']
print(varlist1.count('grape'))

# append(), 返回值为 None
varlist1.append('Lemon')
print(varlist1)

# insert(): 向列表中指定的index位置添加元素
varlist1.insert(3, 'banana')
print(varlist1)

# pop(): 指定的索引位置上元素弹出
varlist1.pop(3)
print(varlist1)

# remove(): 通过一个值来弹出, 只弹出第一个值
varlist1.remove('orange')
print(varlist1)

# index(): 寻找指定的元素第一次出现的位置，如果找不到则抛出异常
res = varlist1.index('grape', 2, 7)
print(res)

# extend(): 
# varlist1.extend([1, 2, 3, '123'])
# varlist1.extend('123')
varlist1.extend(['123'])
print(varlist1)

# reverse(): 列表翻转
varlist1.reverse()
print(varlist1)

# varlist1.clear()
# print(varlist1)

# sort(): 对列表进行排序
varlist1 = ['apple', 'orange', 'grape', 'peach', 'watermelon', 'grape', 'banana', 'lime', 'lemon', 'tangelo']
varlist1.sort()
print(varlist1)

varlist1 = [1, -2, 3, 5, 7, 9]
varlist1.sort()
print(varlist1)
varlist1.sort(key=abs)
print(varlist1)

# copy() 复制元素
# 对于多维数组，copy之后，对多维列表中元素进行操作会同时影响两个数组
res= varlist1.copy()
print(res)
print(varlist1)

del res[2]
print(res)
print(varlist1)

varlist1 = ['1', '2', [1, 2, 3]]
res = varlist1.copy()

del res[2][1]
print(res)
print(varlist1)
