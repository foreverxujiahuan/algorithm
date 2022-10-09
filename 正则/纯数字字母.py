import re

pattern = re.compile("^[0-9A-Za-z]+$")

ans = pattern.match("1")
print(ans)
