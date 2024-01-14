import re

s = "deded"
e = "ded"

ans = re.finditer(e, s,flags=1)
#
# ans = s.find("e")
# print(ans)
index = [i.start() for i in ans]
print(index)