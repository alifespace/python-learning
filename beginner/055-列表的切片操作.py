varlist1 = ['apple', 'orange', 'peach', 'watermelon', 'grape', 'banana', 'lime', 'lemon', 'Tangelo']

res = varlist1[2::2]
print(res)

# 倒序输出
res = varlist1[::-1]
print(res)

# 对原来列表的替换，对容器类型数据会拆分成每个元素
varlist1[2:4] = 'Yuzu'
print(varlist1)

varlist1 = ['apple', 'orange', 'peach', 'watermelon', 'grape', 'banana', 'lime', 'lemon', 'Tangelo']
varlist1[2::2] = 'Yuzu'
print(varlist1)

varlist1 = ['apple', 'orange', 'peach', 'watermelon', 'grape', 'banana', 'lime', 'lemon', 'Tangelo']
del varlist1[2:6:2]
print(varlist1)