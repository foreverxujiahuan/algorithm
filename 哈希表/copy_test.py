from copy import deepcopy

d = {'a': []}
v = deepcopy(d['a'])
v.append(1)
print(d)
