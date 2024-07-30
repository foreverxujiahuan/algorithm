

from collections import defaultdict
import random

d = defaultdict(list)

d['a'].append(1)
d['a'].append(2)

ans = random.choice(list(d.keys()))
print(ans)