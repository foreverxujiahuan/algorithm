import re


s = "https://h5.m.taobao.com/awp/core/detail.htm?id=767934266790&skuId=5272528281487"
p = "https://h5.m.taobao.com/awp/core/detail.htm\\?id=\\d+[-A-Za-z0-9+&@#/%?=~_|!:,.;]*"
pp = re.compile(p)
ans = pp.match(s)
print(ans)