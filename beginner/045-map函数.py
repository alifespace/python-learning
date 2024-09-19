'''
map()
'''

oldlist = ['1', '2', '3', '4']
newlist = []

res = map(int, oldlist)
print(list(res), type(res))

oldlist = [1, 2, 3, 4]
res = map(lambda x:x**2, oldlist)
print(res, type(res))
print(list(res))
