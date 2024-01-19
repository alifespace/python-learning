#推导式(compcomprehensions)

# 列表推导式
vec1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
vect1_flat = [num for elem in vec1 for num in elem]
print(vect1_flat)

list1 = [(x, y) for x in [1, 2, 3] for y in[3, 1, 4] if x!=y]
print(list1)

# 字典推导式
dict1 = {'a':10, 'b':20, 'c':30}
dict1_exg = {v : k for k, v in dict1.items()}
print(dict1_exg)

# 集合推导式
set1 = {x**2 for x in [1, -2, 2, 3]}
print(set1)
