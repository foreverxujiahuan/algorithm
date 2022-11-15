import re

pattern = re.compile("\d+")

s = "124f"
ans = pattern.fullmatch(s)
print(ans)