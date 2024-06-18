# 把字典的键值对转换为格式"a=b"
dict1 = {'user': 'admin', 'age': 20, 'phone': '133'} 
varlist1 = []
for key, value in dict1.items():
    varlist1.append(key + '=' + str(value))

print(varlist1)

varlist2 = [k + '=' + str(v) for k, v in dict1.items()]
print(varlist2)

# 把列表中的所有字符转换为小写
varlist1 = ['AAAAA', 'bbBb', 'CCcCc']
varlist2 = [item.lower() for item in varlist1]
print(varlist2)

# x 是0～5之间的偶数，y是0～5之间的计数，组成（x，y）
varlist1 = [(2*x, 2*y+1) for x in range(6) if 2*x <= 5 for y in range(6) if (2*y+1)<=5]
print(varlist1)

# 求M，N的乘积
M = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
N = [
        [2, 2, 2],
        [3, 3, 3],
        [4, 4, 4]
]

list1 = [[M[i][j] * N[i][j] for j in range(3)] for i in range(3)]
print(list1)