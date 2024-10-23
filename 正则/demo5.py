import re

# 你的链接匹配正则表达式
link_pattern = "|".join([
    "https?://item.taobao.com/item.html?\\?id=\\d+[-A-Za-z0-9+&@#/%?=~_|!:,.;]*",
    "https?://item.taobao.com/item.html?\\?.*&id=\\d+[-A-Za-z0-9+&@#/%?=~_|!:,.;]*",
    "https?://detail.tmall.com/item.html?\\?id=\\d+[-A-Za-z0-9+&@#/%?=~_|!:,.;]*",
    "https?://detail.tmall.com/item.html?\\?.*&id=\\d+[-A-Za-z0-9+&@#/%?=~_|!:,.;]*",
    "https?://detail.tmall.hk/hk/item.html?\\?id=\\d+[-A-Za-z0-9+&@#/%?=~_|!:,.;]*",
    "https?://detail.tmall.hk/hk/item.html?\\?.*&id=\\d+[-A-Za-z0-9+&@#/%?=~_|!:,.;]*",
    "https?://h5.m.taobao.com/awp/core/detail.html?\\?id=\\d+[-A-Za-z0-9+&@#/%?=~_|!:,.;]*",
    "https?://h5.m.taobao.com/awp/core/detail.html?\\?.*id=\\d+[-A-Za-z0-9+&@#/%?=~_|!:,.;]*",
    "https?://main.m.taobao.com/security-h5-detail/home\\?id=\\d+[-A-Za-z0-9+&@#/%?=~_|!:,.;]*"
])

# 匹配整个 JSON 字符串的正则表达式
json_pattern = fr'{{"text":"({link_pattern})","jsview":\[{{"value":{{"url":"({link_pattern})","name":"({link_pattern})","safe":"SAFE"}},"type":1}}]}}'

# 示例 JSON 数据
json_data = '{"text":"https://item.taobao.com/item.htm?id=742782571740","jsview":[{"value":{"url":"https://item.taobao.com/item.htm?id=742782571740","name":"https://item.taobao.com/item.htm?id=742782571740","safe":"SAFE"},"type":1}]}'

# 正则匹配
# match = re.match(json_pattern, json_data)
# if match:
#     print("Matched URLs:", match.groups())
# else:
#     print("No match")

final_pattern = link_pattern + "|" + json_pattern

pattern = re.compile(final_pattern)
ans = pattern.match(json_data)
print(ans)
print(len(json_data))

ans = pattern.match("https://item.taobao.com/item.htm?id=742782571740")
print(ans)
print(len("https://item.taobao.com/item.htm?id=742782571740"))