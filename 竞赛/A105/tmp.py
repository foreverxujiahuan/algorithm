from itertools import permutations


l = 5
cur = permutations(range(l), 5)
for t in cur:
    print(t)