from collections import defaultdict
import random


cat2intent_content_dict = defaultdict(dict)

cat2intent_content_dict['a'].setdefault('b', []).append(1)

# print(cat2intent_content_dict)


d = {'a':1,
     'b':2}

ans = random.choice(d.values())
print(ans)