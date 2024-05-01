oldlist = [1, 2, 3]
newlist = oldlist.copy()

print(oldlist, id(oldlist))
print(newlist,id(newlist))

oldlist = [[1,2,3], ['a', 'b', 'c']]
newlist = oldlist.copy()

print(id(oldlist[1][1]))
print(id(newlist[1][1]))
del newlist[1][1]
print(oldlist)

import copy
oldlist = [[1,2,3], ['a', 'b', 'c']]
newlist = copy.deepcopy(oldlist)
print(id(oldlist[1]))
print(id(newlist[1]))