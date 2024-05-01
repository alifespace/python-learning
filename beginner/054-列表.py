varlist1 = [1, 2, 3, 4]
varlist2 = ['a', 'b', 'c', 'd']

#列表的拼接
res = varlist1 + varlist2
print(res)

# 列表元素的重复
res = varlist1 * 3
print(res)

# 检测元素是否存在于列表之中
res = 'a' in varlist2
print(res)

# 列表的索引操作
print(varlist2[-2])

# 向列表中添加元素
varlist2.append(['ff', 'gg'])
print(varlist2)

# 获取列表的长度
print(len(varlist2))

# 列表元素的删除
del(varlist2[2])
print(varlist2)
res = varlist2.pop()
print(varlist2, res)