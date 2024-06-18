varlist1 = []
for i in range(10):
    varlist1.append(i**2)

print(varlist1)

varlist1 = []
varlist1 = list(map(lambda x:x**2, range(10)))
print(varlist1)

data1 = [x**2 for x in range(10)]
print(data1)

data1 = "1234"
data1 = [int(i)*2 for i in data1]
print(data1)

# 带判断条件的列表推导式
data1 = [i for i in range(10) if i % 2 == 0]
print(data1)

data1 = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(data1)

# 嵌套的列表推导式
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
res = [[row[i] for row in matrix]for i in range(4)]
print('res:', res)

for row in matrix:
    print(row)


# 九九乘法表
res = [[i*j for j in range(1, i+1)] for i in range(1, 10)]
for row in res:
    print(row)