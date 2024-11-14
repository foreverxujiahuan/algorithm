import re

pattern = r'[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?'

text = "124214e10是"

regex = re.compile(pattern)

ans = regex.fullmatch(text)

print(ans)