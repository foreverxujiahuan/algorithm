from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    hash_table = dict()
    for s in strs:
        t = ''.join(sorted(s))
        if t in hash_table.keys():
            hash_table[t].append(s)
        else:
            hash_table[t] = [s]
    res = []
    for k,v in hash_table.items():
        res.append(v)
    return res


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
res = groupAnagrams(strs)
print(res)
