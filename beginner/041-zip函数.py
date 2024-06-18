var1 = [1, 2, 3, 4, 5]
var2 = ['a', 'b', 'c']
var3 = ('1', '2')

res = zip(var1, var2, var3)
print(list(res))

x = [1, 2, 3]
y = [4, 5, 6]
x2 = zip(*zip(x))
print(list(x2))
print(*zip(x, y)) # 组合好后的元组数据
print(list(zip(x, y)))
