import re

def numberOfWays(s: str) -> int:
    pattern = re.compile(".*0.*1.*0.*")

res = numberOfWays("001101")
print(res)
